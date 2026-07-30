# Day 47 – Google Cloud: Storage Classes

## Objective

Understand the different storage classes available in Google Cloud Storage, their use cases, pricing considerations, and how to select the appropriate class based on data access patterns.

---

# What are Storage Classes?

A Storage Class defines how frequently data is expected to be accessed and how it is stored.

Choosing the correct storage class helps optimize storage costs while maintaining the required level of availability and performance.

---

# Why are Storage Classes Important?

Different data has different access patterns.

Examples:

- Website images are accessed frequently.
- Backup files are accessed occasionally.
- Archived records may not be accessed for years.

Using the appropriate storage class reduces storage costs.

---

# Types of Storage Classes

Google Cloud provides four primary storage classes.

---

## Standard Storage

Designed for data accessed frequently.

Characteristics:

- Low latency
- High availability
- No minimum storage duration

Common uses:

- Websites
- Mobile applications
- Streaming media
- Frequently accessed files

---

## Nearline Storage

Designed for data accessed about once per month.

Characteristics:

- Lower storage cost
- Small retrieval cost
- Minimum storage duration of 30 days

Common uses:

- Monthly backups
- Disaster recovery
- Long-term data retention

---

## Coldline Storage

Designed for data accessed once every three months.

Characteristics:

- Lower storage cost than Nearline
- Higher retrieval cost
- Minimum storage duration of 90 days

Common uses:

- Quarterly backups
- Compliance data
- Archived business files

---

## Archive Storage

Designed for data rarely accessed.

Characteristics:

- Lowest storage cost
- Highest retrieval cost
- Minimum storage duration of 365 days

Common uses:

- Historical records
- Legal documents
- Long-term archives
- Regulatory compliance

---

# Comparison of Storage Classes

| Storage Class | Access Frequency | Typical Use Case |
|---------------|------------------|------------------|
| Standard | Frequent | Websites, applications |
| Nearline | Monthly | Backups |
| Coldline | Quarterly | Archived business data |
| Archive | Rarely | Long-term storage |

---

# Choosing the Right Storage Class

Consider:

- How often the data is accessed.
- How quickly it must be retrieved.
- Storage budget.
- Business requirements.

Frequently accessed data should remain in Standard Storage, while archived data is better suited for Archive Storage.

---

# Advantages

- Lower storage costs
- Flexible data management
- Improved cost optimization
- Multiple options for different workloads

---

# Best Practices

- Store active application data in Standard Storage.
- Use Nearline for monthly backups.
- Move older backups to Coldline or Archive.
- Review storage usage regularly.
- Select the storage class based on actual access patterns rather than storage size.

---

# Real-World Example

A media company stores current video content in **Standard Storage** for quick access.

After six months, older videos are moved to **Coldline Storage**, and after several years they are archived using **Archive Storage**. This strategy reduces storage costs while ensuring the data remains available when needed.

---

# What I Learned

- Storage Classes determine how data is stored and accessed.
- Google Cloud provides Standard, Nearline, Coldline, and Archive Storage.
- Different storage classes are optimized for different access patterns.
- Choosing the correct storage class helps reduce storage costs.
- Data can be moved between storage classes as business needs change.
