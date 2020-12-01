import torch
from torch.utils.data import DataLoader, Dataset
from typing import Any, NoReturn

class TextDataset():
    '''
        custom dataset class TextDatasets, to create the torch dataset
        
        Attributes:
            data (Any): data either pandas df or transformers TextDataset or
            tokenizer (Any): tokenizer that will be used to tokenize the text
            input_field (str, optional): name of the input field in df/dataset. Defaults to "text".
            target_field (str, optional): target field name it will be either numerical class or text if task is seq2seq. Defaults to None.
            parallel_corpus (bool, optional): whether corpus is parallel or not. Defaults to False.
            input_len (int, optional): len of the input sequence. Defaults to 512.
            output_len (int, optional): output sequence length. Defaults to None.
            attention_mask (bool, optional): attention mask, for pad tokens it will be 0 and for input tokens it will 10. Defaults to True.

    '''
    
    def __init__(self, 
                data:Any,
                tokenizer:Any, 
                input_field:str="text", 
                target_field:str=None, 
                parallel_corpus:bool=False,
                input_len:int=512, 
                output_len:int=None,
                attention_mask:bool=True)->None:
        
        """
            Args:
            data (Any): data either pandas df or transformers TextDataset or
            tokenizer (Any): tokenizer that will be used to tokenize the text
            input_field (str, optional): name of the input field in df/dataset. Defaults to "text".
            target_field (str, optional): target field name it will be either numerical class or text if task is seq2seq. Defaults to None.
            parallel_corpus (bool, optional): whether corpus is parallel or not. Defaults to False.
            input_len (int, optional): len of the input sequence. Defaults to 512.
            output_len (int, optional): output sequence length. Defaults to None.
            attention_mask (bool, optional): attention mask, for pad tokens it will be 0 and for input tokens it will 10. Defaults to True.
        """
        
        # ''' Sanity Checking'''
        assert output_len is None and parallel_corpus==False, "When parallel_corpus=True both input and output should be text fields"
        
        
        self.input = data[input_field]
        
        self.target_field = target_field
        
        if target_field is not None:
            self.target = data[target_field]
            
        self.parallel_corpus=parallel_corpus
        
        self.tokenizer = tokenizer
        
        self.input_len = input_len
        self.output_len = output_len
        
        self.attention_mask = attention_mask
        
        
    
    def __len__(self)->int:
        """
        _len__ method of custom datasets class

        Returns:
            int: number of samples in your dataset
        """
       
        return len(self.input)
    
    def __getitem__(self, index)->dict:
        
        input = self.input[index]
        
        if self.target_field is not None:
            target =  self.target[index]
        
        input_encoding = self.tokenizer.encode_plus(
            text=input,
            padding='max_length',
            truncation=True,
            max_length=self.input_len,
            return_tensors='pt',
            return_attention_mask=True,
        )
        input_ids = input_encoding['input_ids'].squeeze()
        input_mask = input_encoding['attention_mask'].squeeze()
        
        """If parallel_corpus==False and target_field==None, which means this is parallel corpus task ie: MT, SqUAD """
        if self.parallel_corpus==True:
            target = self.target[index]
            target_encoding = self.tokenizer.encode_plus(
                text=target,
                padding='max_length',
                truncation=True,
                max_length=self.output_len,
                return_tensors='pt',
                return_attention_mask=True,
            )
            target_ids = target_encoding['input_ids'].squeeze()
            target_mask = target_encoding['targte_mask'].squeeze()
            return {
                "input_text":input,
                "input_ids":input_ids,
                "input_mask":input_mask,

                "target_text":target,
                "target_ids":target_ids,
                "target_mask":target_mask,
            }
        # When data belongs to sequence labelling task
        elif self.target_field is not None:
            target =  self.target[index]
            return {
                "input_text":input,
                "input_ids":input_ids,
                "input_mask":input_mask,
                "target":torch.tensor([target], dtype=torch.long)
            }
        
        # When data is test set which means no target data at all
        elif self.target_field is None and self.output_len is None:
            return {
                "input_text":input,
                "input_ids":input_ids,
                "input_mask":input_mask,
            }
        
    def __str__(self):
        return "TextDataset"    
    
if __name__=='__main__':
    dataset = TextDataset(data={"text":[], "label":[]}, tokenizer="demo", parallel_corpus=True)
    print(len(dataset))