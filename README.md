# Traffic-ELT Migration
<div id="top"></div>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">Traffic-ELT Migration</h3>

  <p align="center">
    A dockerized ELT Migration pipeline.
    <br />
    <a href="#"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/abreham-g/Traffic-ELT/issues">Report Bug</a>
    ·
    <a href="https://github.com/abreham-g/Traffic-ELT/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
<!-- ![ELT](screenshots/traffic-elt-migration.jpg) -->
A dockerized Extract, Load, Transform (ELT) pipeline with MySQL, Airflow, DBT, and a Apache Superset.

### Built With

Tech Stack used in this project
* [![Docker][Docker.com]][Docker-url]
* [![MySQL][Mysql.com]][Mysql-url]
* [![Airflow][Airflow.com]][Airflow-url]
* [![DBT][DBT.com]][DBT-url]
* [![Superset][Superset.com]][Superset-url]

<!-- GETTING STARTED -->
## Getting Started
### Prerequisites
Make sure you have docker installed on local machine.
-   Docker
-   Docker Compose

### Installation

1. Clone the repo
    ```sh
    git clone https://github.com/abreham-g/ELT-Traffic-Migration-Data.git
    ```
2. Navigate to the folder
    ```sh
    cd ELT-Traffic-Migration-Data
    ```
    
3. Build an airflow image
    ```sh
    docker build . --tag apache_dbt/airflow:2.3.3
    ```
4. Run
    ```sh
     docker-compose up
    ```
5. Open Airflow web browser
    ```JS
    Navigate to `http://localhost:8080/` on the browser
    activate and trigger load_dag
    activate and trigger dbt_dag
    ```
6. Access Apache Superset dashboard
    ```JS
    Navigate to `http://localhost:8088/` on the browser
    ```

<!-- CONTRIBUTING -->
## Contributing
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License
Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contributor
Abreham Gessesse - Aynuyeabresh@gmail.com

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
-   [10 Academy](https://www.10academy.org/)



<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/abreham-g/ELT-Traffic-Migration-Data.svg?style=for-the-badge
[contributors-url]: https://github.com/abreham-g/ELT-Traffic-Migration-Data/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/abreham-g/ELT-Traffic-Migration-Data.svg?style=for-the-badge
[forks-url]: https://img.shields.io/github/forks/abreham-g/ELT-Traffic-Migration-Data?style=for-the-badge
[stars-shield]: https://img.shields.io/github/stars/abreham-g/ELT-Traffic-Migration-Data?style=for-the-badge
[stars-url]: https://github.com/abreham-g/ELT-Traffic-Migration-Data/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://img.shields.io/github/issues/DiyeMark/Traffic-ELT?style=for-the-badge
[license-shield]: https://img.shields.io/github/license/abreham-g/ELT-Traffic-Migration-Data?style=for-the-badge
[license-url]: https://github.com/DiyeMark/Traffic-ELT/blob/main/LICENSE
[Postgresql.com]: https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white
[Postgresql-url]: https://www.postgresql.org/
[Mysql.com]: https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white
[Mysql-url]: https://www.mysql.com
[Airflow.com]: https://img.shields.io/badge/Airflow-017CEE?style=for-the-badge&logo=Apache%20Airflow&logoColor=white
[Airflow-url]: https://airflow.apache.org/
[Docker.com]: https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com/
[DBT.com]: https://img.shields.io/badge/DBT-FF694B?style=for-the-badge&logo=dbt&logoColor=white
[DBT-url]: https://docs.getdbt.com/
[Superset-url]: https://superset.apache.org
