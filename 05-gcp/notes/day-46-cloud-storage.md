# Day 46 – Google Cloud: Cloud Storage

## Objective

Understand what Google Cloud Storage is, how object storage works, its key components, and how it is used to securely store and manage data in Google Cloud.

---

# What is Google Cloud Storage?

Google Cloud Storage (GCS) is Google's object storage service that allows users to store and retrieve any amount of data from anywhere in the world.

Unlike disks attached to Virtual Machines, Cloud Storage stores files as objects inside containers called buckets.

It is designed to provide high durability, scalability, and availability for all types of data.

---

# Why Use Cloud Storage?

Cloud Storage is commonly used because it provides:

- Unlimited scalability
- High durability
- Secure storage
- Global accessibility
- Pay-as-you-go pricing
- Integration with other Google Cloud services

It can store files ranging from a few bytes to several terabytes.

---

# Object Storage

Cloud Storage is an object storage system.

Each stored file is called an **Object**.

An object consists of:

- File data
- Metadata
- Unique object name

Example:

```text
Bucket
│
├── image.jpg
├── report.pdf
└── backup.zip
```

---

# What is a Bucket?

A Bucket is a container that stores objects.

Before uploading any file, a bucket must be created.

Each bucket has:

- A globally unique name
- A storage location
- A storage class
- Access permissions

Example:

```text
my-company-backups
```

---

# Bucket Naming Rules

Bucket names:

- Must be globally unique.
- Can contain lowercase letters, numbers, hyphens (-), underscores (_), and periods (.).
- Cannot contain spaces.
- Cannot be changed after creation.

Example:

```text
company-backups-2026
```

---

# Objects

Objects are the actual files stored inside a bucket.

Examples:

- Images
- Videos
- Documents
- Application backups
- Log files
- Machine learning datasets

Each object has metadata such as:

- Name
- Size
- Creation time
- Storage class

---

# Storage Locations

Buckets can be created in different locations.

### Regional

Stores data in one region.

Example:

```text
asia-south1
```

---

### Dual-Region

Stores data across two regions.

Provides higher availability.

---

### Multi-Region

Stores data across multiple geographic regions.

Provides low latency for users worldwide.

---

# Advantages of Cloud Storage

- Highly durable
- Secure
- Scalable
- Cost-effective
- Easy to manage
- Accessible through APIs and the Cloud Console

---

# Common Use Cases

Cloud Storage is used for:

- Website assets
- File uploads
- Database backups
- Disaster recovery
- Log storage
- Data analytics
- Media storage

---

# Best Practices

- Choose the correct storage location.
- Enable versioning for important data.
- Apply IAM permissions to buckets.
- Delete unused objects regularly.
- Encrypt sensitive data.

---

# Real-World Example

An online learning platform stores course videos, PDF notes, and images in Google Cloud Storage.

Students download the files from Cloud Storage while the application servers focus only on processing user requests, improving performance and scalability.

---

# What I Learned

- Google Cloud Storage is an object storage service.
- Files are stored as objects inside buckets.
- Buckets must have globally unique names.
- Cloud Storage is highly durable and scalable.
- It is widely used for backups, media, and application data.
