# AWS Data Pipeline using PySpark & EMR

## 🚀 Overview
This project demonstrates a scalable end-to-end data pipeline built using AWS services and PySpark for processing large-scale data.

## 🛠 Technologies Used
- PySpark
- AWS EMR
- AWS S3
- AWS Step Functions
- Snowflake
- Python

## 📊 Features
- Processes large-scale data (~4TB)
- Handles multiple data sources (S3, Snowflake, Web API)
- ETL pipeline implementation
- Distributed data processing using Spark

## ⚡ Optimization Techniques
- Broadcast Join to reduce shuffle
- Data Skew handling using salting
- Partition tuning for performance improvement

## 🔄 Workflow
1. Data ingestion from S3, Snowflake, and API
2. Transformation using PySpark
3. Intermediate data stored in S3
4. Final data written to S3 and ElasticSearch
5. Orchestration using AWS Step Functions

## 🧠 Key Learnings
- Handling large-scale distributed data
- Spark optimization techniques
- AWS-based data pipeline design

## 📁 Project Structure
- pipeline.py → Main PySpark job
- README.md → Project documentation

