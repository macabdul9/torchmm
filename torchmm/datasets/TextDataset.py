from torch.utils.data import DataLoader, Dataset
from typing import Any, NoReturn

class TextDataset(Dataset):
    
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
        __init__() of custom dataset class TextDataset

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
        
        ''' Sanity Checking'''
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
    
    def __getitem__(self, index):
        input = self.input[index]
        if self.target_field is not None:
            target =  self.target[index]
        
        encoding = self.tokenizer.encode_plus(
            
        )
    
    def __str__(self):
        return "TextDataset"    
    
if __name__=='__main__':
    dataset = TextDataset(data={"text":[], "label":[]}, tokenizer="demo", parallel_corpus=True)
    print(len(dataset))