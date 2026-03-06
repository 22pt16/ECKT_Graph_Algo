Assumptions:
1 Synthetic node attributes generated due to lack of attributes in Facebook dataset.
2 Income treated as sensitive attribute.
3 k-anonymity enforced by merging clusters smaller than k.
4 Age and location generalized to ranges to hide individual identity.
5 t-closeness measured using distribution difference.
6 K-means++ used for clustering nodes based on attributes.


Features used (quassi):
    age
    gender
    location

Sensitive attribute:
    income