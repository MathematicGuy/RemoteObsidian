Predict Next-Token using RNN language model [code](https://colab.research.google.com/drive/1kQvHhQ7VjEMw8rSyz5d95dG9y8Rag26F#scrollTo=E_PsrB_cU34-)

Tokenizer(`stride=[overlap_count]`)
-> Number of Overlap token sequence is longer than max_length. Help to preserve Token between sequence transition.
	e.g. Sentence 1 end with `[...,like,ice cream]` and Sentence 2 start with `[like,ice cream,...]`  
**Example Scenario** If you have a `max_length` of 10 and a `stride` of 3:
- **Chunk 1:** Tokens 1 through 10.
- **Chunk 2:** Tokens 8 through 17 (starts at 11 - 3 = 8).
- **Overlap:** Tokens 8, 9, and 10 appear in both chunks


