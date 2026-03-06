# Enhanced Clustering-Based (k,t)-Anonymity for Graphs

**Implementation of the ECKT Privacy-Preserving Algorithm for Social Network Data**

---

## 1. Project Overview

This project implements a **privacy-preserving graph anonymization algorithm** inspired by the **Enhanced Clustering-Based (k,t)-Anonymity (ECKT)** method for social network data.

Social networks often contain **sensitive user information**. When such datasets are published for research or analytics, there is a risk of:

* **Identity disclosure** – identifying an individual node
* **Attribute disclosure** – inferring sensitive attributes of users

To mitigate these risks, this project applies **k-anonymity and t-closeness** to a social network dataset using clustering-based anonymization.

The implementation uses **k-means++ clustering combined with cluster balancing and attribute generalization** to produce anonymized graph data while preserving useful structural properties.

---

## 2. Dataset

This project uses the **Facebook social network dataset** from the SNAP repository.

Dataset statistics:

| Property               | Value |
| ---------------------- | ----- |
| Nodes                  | 4039  |
| Edges                  | 88234 |
| Average Degree         | 43.69 |
| Clustering Coefficient | 0.605 |

The dataset contains only graph structure (edges). Since node attributes are not provided, **synthetic attributes are generated for experimentation**.

Generated attributes:

| Attribute       | Type        | Description                           |
| --------------- | ----------- | ------------------------------------- |
| age             | Numeric     | User age                              |
| gender          | Binary      | Gender indicator                      |
| location        | Categorical | Region identifier                     |
| income_numeric  | Numeric     | Simulated income                      |
| income_category | Categorical | Sensitive attribute (low/medium/high) |

---

## 3. Privacy Model

### k-Anonymity

k-anonymity ensures that each individual record is indistinguishable from at least **k-1 other records** with respect to quasi-identifiers.

In this project:

```
k = 10
```

Each node should belong to a cluster containing **at least 10 nodes**.

---

### t-Closeness

t-closeness prevents **attribute disclosure** by ensuring that the distribution of a sensitive attribute within a cluster is close to the distribution of the entire dataset.

Sensitive attribute used:

```
income_category
```

t-closeness threshold:

```
t = 0.7
```

Clusters exceeding this threshold are considered to violate attribute privacy.

---

## 4. Algorithm Pipeline

The implemented workflow follows the ECKT framework.

### Step 1 — Load Graph

The Facebook graph is loaded using NetworkX.

---

### Step 2 — Generate Node Attributes

Synthetic attributes are assigned to nodes because the dataset does not include user features.

---

### Step 3 — Clustering (k-means++)

Nodes are grouped into clusters using **k-means++ initialization** based on:

```
age
gender
location
income_numeric
```

Clusters generated:

```
20 clusters
```

---

### Step 4 — Distance Matrix Assignment

To approximate the ECKT algorithm, distances between nodes and cluster centroids are computed and nodes are assigned based on sorted distance pairs. This helps balance cluster sizes.

---

### Step 5 — k-Anonymity Enforcement

Clusters smaller than **k=10** are merged with larger clusters to guarantee the anonymity requirement.

---

### Step 6 — Attribute Generalization

Quasi-identifiers are generalized to reduce identifiability.

Examples:

| Original     | Generalized |
| ------------ | ----------- |
| Age = 22     | 18–30       |
| Location = 1 | Region-A    |

---

### Step 7 — t-Closeness Verification

The distribution of `income_category` within each cluster is compared with the global distribution.

Clusters satisfying the t-closeness threshold are considered **privacy-safe**.

---

### Step 8 — Evaluation Metrics

The anonymized dataset is evaluated using:

**Cluster Size Distribution**

Measures the number of users in each cluster.

**Degree of Anonymization**

Average cluster size.

**Information Loss**

Measures how much variance in sensitive attributes is lost after anonymization.

---

## 5. Experimental Results

Graph statistics:

```
Nodes: 4039
Edges: 88234
Average degree: 43.69
Clustering coefficient: 0.605
```

Privacy evaluation:

| Metric                          | Result  |
| ------------------------------- | ------- |
| Total clusters                  | 20      |
| Average cluster size            | 201.95  |
| k-anonymity requirement         | 10      |
| Achieved anonymity level        | ≈202    |
| Clusters satisfying t-closeness | 15 / 20 |
| Information loss                | 0.00245 |

Interpretation:

* Each node is indistinguishable among ~200 users.
* 75% of clusters satisfy attribute privacy constraints.
* Information loss is extremely low (≈0.24%).

This demonstrates that the anonymization process **provides strong privacy protection while maintaining high data utility**.

---

## 6. Output Files

The program produces the following outputs:

```
output/
 ├── anonymized_data.csv
 ├── summary_metrics.csv
 └── cluster_distribution.png
```

Descriptions:

* **anonymized_data.csv** – anonymized dataset with cluster labels
* **summary_metrics.csv** – evaluation metrics summary
---

## 7. Project Structure and execution

```
ECKT_Graph_Algo
│
├── data
│   └── facebook_combined.txt
│
├── src
│   ├── load_graph.py
│   ├── generate_attributes.py
│   ├── clustering.py
│   ├── kanonymity.py
│   ├── generalization.py
│   ├── tcloseness.py
│   ├── evaluation.py
│   └── visualization.py
│
├── output
│   ├── anonymized_data.csv
│   ├── summary_metrics.csv
│   └── cluster_distribution.png
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 8. Installation

Install dependencies:

```
pip install -r requirements.txt
```

Required libraries include:

```
networkx
pandas
numpy
scikit-learn
matplotlib
scipy
```

---

## 9. Running the Project

Execute:

```
python main.py
```

The program will:

1. Load the graph
2. Generate attributes
3. Run clustering
4. Apply privacy mechanisms
5. Evaluate anonymization quality
6. Save results to the `output` folder

---

## 10. Assumptions

Several assumptions were made to implement the algorithm:

1. Facebook dataset lacks node attributes; therefore synthetic attributes were generated.
2. `income_category` is treated as the **sensitive attribute**.
3. Age, gender, and location act as **quasi-identifiers**.
4. Small clusters are merged to enforce k-anonymity.
5. Attribute generalization is used to reduce identity disclosure risk.
6. t-closeness is approximated using distribution difference.

---

## 11. Applications

This approach is useful for:

* Publishing anonymized social network datasets
* Privacy-preserving data mining
* Secure data sharing
* Social network analysis under privacy constraints

---

## 12. Conclusion

This project demonstrates a clustering-based approach to anonymizing graph data while preserving structural properties of social networks.

Results show that:

* Strong anonymity guarantees can be achieved
* Attribute disclosure risks can be reduced
* Data utility remains high

The approach successfully balances **privacy protection and analytical usefulness** for social network datasets.

---

