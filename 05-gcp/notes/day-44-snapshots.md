# Day 44 – Google Cloud: Snapshots

## Objective

Understand what Snapshots are in Google Compute Engine, how they are used for backup and disaster recovery, and learn best practices for protecting virtual machine data.

---

# What is a Snapshot?

A Snapshot is a backup of a Persistent Disk in Google Compute Engine.

Snapshots capture the data stored on a disk at a specific point in time. They can later be used to restore data or create new disks.

Snapshots are stored securely in Google Cloud Storage and are independent of the original Virtual Machine.

---

# Why are Snapshots Important?

Snapshots help organizations:

- Protect important data
- Recover from accidental deletion
- Restore systems after failures
- Migrate workloads
- Create identical environments

They are an essential part of backup and disaster recovery planning.

---

# How Snapshots Work

When a snapshot is created:

1. Google copies the data from the Persistent Disk.
2. The snapshot is stored securely.
3. The original VM continues running.
4. The snapshot can later be used to create a new disk.

```text
Persistent Disk
        │
        ▼
    Snapshot
        │
        ▼
 New Persistent Disk
```

---

# Incremental Snapshots

Google Cloud uses **incremental snapshots**.

The first snapshot stores all the disk data.

Future snapshots store only the changes made since the previous snapshot.

Benefits include:

- Reduced storage usage
- Faster backup creation
- Lower storage costs

---

# Creating a Snapshot

The general process is:

1. Select the Persistent Disk.
2. Choose **Create Snapshot**.
3. Provide a snapshot name.
4. Save the snapshot.

The snapshot becomes available for future recovery.

---

# Restoring from a Snapshot

A snapshot cannot be attached directly to a VM.

Instead:

1. Create a new Persistent Disk from the snapshot.
2. Attach the new disk to an existing or new Virtual Machine.

This restores the backed-up data.

---

# Common Use Cases

Snapshots are commonly used for:

- Backup
- Disaster Recovery
- Testing
- Cloning environments
- System migration

---

# Best Practices

- Schedule regular snapshots.
- Keep multiple recovery points.
- Delete outdated snapshots when no longer needed.
- Test backup restoration periodically.
- Create snapshots before major system updates.

---

# Real-World Example

Before upgrading a production application, a company creates snapshots of all Compute Engine disks.

If the upgrade fails, they restore the disks from the snapshots and quickly recover the previous working environment.

---

# What I Learned

- Snapshots are backups of Persistent Disks.
- They support backup and disaster recovery.
- Google Cloud uses incremental snapshots.
- Snapshots can be used to create new Persistent Disks.
- Regular snapshots help protect important business data.
