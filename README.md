# On the Selection of Positive and Negative Samples for Contrastive Math Word Problem Neural Solver

Solving math word problems (MWPs) involves uncovering logical relationships among quantities in natural language descriptions of math problems. Recent studies have demonstrated that the contrastive learning framework can assist models in identifying semantically similar examples while distinguishing between different mathematical logics. This alleviates models' dependence on shallow heuristics for predicting problem solutions. However, we have observed significant disparities in the positive and negative sample selections among different contrastive learning frameworks, which can sometimes exhibit complete contradictions. This discrepancy is attributed to the lack of an effective criterion for evaluating the distance between the mathematical logics of word problems.
To address this issue, we introduce a novel formula for evaluating mathematical equation similarity in the context of word problem association. Our formula enables flexible focus on either global or local differences in the mathematical logic, thereby implementing distinct criteria for similarity calculation. 
We investigate the impact of various positive and negative sample selection strategies on contrastive learning models using the proposed formula in order to identify the optimal strategy. Our experimental results reveal substantial performance improvements over existing baselines, highlighting the effectiveness of our approach.

## Data

Math23k, MathQA, AsDiv-A data used for this paper could be found in /data folder. We have selected positive and negative samples for each sample according to the method described in the paper.

## Code

For reproducing results, please run:

```python
python train_cl.py
```