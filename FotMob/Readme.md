# ETL Project Using Airflow, PostgreSQL, and Docker

## Table of Contents

1. [Introduction](#introduction)
2. [Project Architecture](#project-architecture)

## Introduction

This project demonstrates a complete ETL (Extract, Transform, Load) pipeline using Apache Airflow, PostgreSQL, and Docker to fetch and process football data from the FotMob API. The goal is to extract match data, transform it, and load it into a PostgreSQL database for further analysis.

## Project Architecture

The project consists of the following components:

- **Apache Airflow**: Orchestrates the ETL workflow.
- **PostgreSQL**: Stores the extracted and transformed data.
- **Docker**: Containerizes the Airflow and PostgreSQL services for easy setup and deployment.

