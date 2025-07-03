# Analysis

## Layer 4, Head 6
This head appears to focus on the previous word for each token in the sentence. For instance, in the example "Do not [MASK] the dog", the token "[MASK]" strongly attends to "not", suggesting a link between modal or auxiliary structures. Similarly, in the second example, many words attend to the word immediately before them, indicating this head might help model local word dependencies.

Example Sentences:

Do not [MASK] the dog

I [MASK] a brand new bag from the shop in the mall down the street.

## Layer 7, Head 1
This head seems to exhibit strong attention from nearly every token to the [CLS] token. This suggests it might be helping to summarize the sentence or contribute to sentence-level understanding, which is consistent with how [CLS] is used in classification tasks.

Example Sentences:

Do not [MASK] the dog

I [MASK] a brand new bag from the shop in the mall down the street.
