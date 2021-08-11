# ICEBERG
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![MIT License][license-shield]][license-url]
[![Organization][organization-shield]][organization-url]
[![Organization][project-shield]][project-url]

<br />
<p align="center">
  <a href="https://github.com/aidenpearce001/Phishing-detection-ML">
    <img src="src/images/logo.jpg" alt="Logo" width="200" height="200">
  </a>

  <h3 align="center">Chongluadao</h3>

  <p align="center">
    [name] is a part of Project ChongLuaDao by using Model Deep Learning to detect the Phishing Website
    <br />
    <a href="http://103.90.227.67:45000/">View Demo</a>
    ·
    <a href="https://github.com/aidenpearce001/Phishing-detection-ML/issues">Report Bug</a>
    ·
    <a href="https://github.com/aidenpearce001/Phishing-detection-ML/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <ul>
          <li><a href="#installation-docker">Install with docker</a></li>
          <li><a href="#installation-python">Install with python</a></li>
        </ul>
      </ul>
    </li>
    <li><a href="#interface">Interface</a></li>
    <li><a href="#model-deep-learning">Phishing Detection Model</a></li>
    <li><a href="#source-for-collecting-data">Dataset</a></li>
    <li><a href="#references">References</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contributors-">Contributor</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
<br/>

## Getting Started
<br/>

### Prerequisites
-   Python **3.7.x** | **3.8.x**
-   docker **1.25.4**
-   docker-compose **1.25.4**

### Installation

#### Installation with Docker
##### Setup the environment file
```bash
mv .env.example .env
```
Make sure the variable `MONGO` is your MongoDB Connection String

##### Download the model weight
Download the model weights <a href="https://drive.google.com/file/d/1RJHlJIvucqEdEhK_Go4hicbM-0Br3WmF/view?usp=sharing">here</a> and put it inside `src/model/weights`
The structure should be as following
```
src
├── model/
    ├── weights
        ├── rf_data_balance.pkl
```

##### Run the service
```bash
docker-compose up
```

#### Installation with Python

##### Setup mongodb
Set up a local MongoDB Service, add the connection string to `.env` file. See the template at `.env.example`

##### Install the required packages
```
cd src && pip install -r requirement.txt
```

##### Download the model weight
Download the model weights <a href="https://drive.google.com/file/d/1RJHlJIvucqEdEhK_Go4hicbM-0Br3WmF/view?usp=sharing">here</a> and put it inside `src/model/weights`
The structure should be as following
```
src
├── model/
    ├── weights
        ├── rf_data_balance.pkl
```

##### Run the server
Run the server with the following command
```
python app.py
```
The server will be up and running on `http://localhost:4500`


### Interface
* `/` Home page of the web interface. Use this to check phishing urls
* `/dashboard` The dashboard with visualizations of the requested urls

### Model Deep Learning

* `CNN`: 
* `Random Forest`: https://drive.google.com/file/d/1RJHlJIvucqEdEhK_Go4hicbM-0Br3WmF/view?usp=sharing

### Source for collecting data
#### Blacklist
- https://phishingreel.io/api/v1/panels/today
- https://api.chongluadao.vn/v1/blacklist
- http://data.phishtank.com/data/online-valid.csv (update every hour)
- https://raw.githubusercontent.com/mitchellkrogza/Phishing.Database/master/phishing-links/output/domains/ACTIVE/list (update every day)

#### Whitelist
- https://api.chongluadao.vn/v1/whitelist
- https://www.alexa.com/topsites/countries/VN
- https://webrank.vn/top-website-vietnam
- https://majestic.com/reports/majestic-million
- https://github.com/csirtgadgets/suspect-domains-dataset/blob/master/whitelist.txt

### References
- http://docnum.univ-lorraine.fr/public/DDOC_T_2015_0058_MARCHAL.pdf
- https://research.aalto.fi/en/datasets/phishstorm-phishing-legitimate-url-dataset
- https://www.sciencedirect.com/science/article/pii/S1877050920310966
- https://www.atlantis-press.com/proceedings/iccsee-13/4487
- https://repository.asu.edu/attachments/189603/content/Namasivayam_asu_0010N_17146.pdf

### License
Distributed under the MIT License. See `LICENSE` for more information.

### Contributors ✨

Thanks goes to these wonderful Penguins

<table>
  <tr>
    <td align="center"><a href="https://github.com/LeDuySon"><img src="https://avatars.githubusercontent.com/u/33374938?v=4" width="100px;" alt=""/><br /><sub><b>Le Duy Son</b></sub></a></td>
    <td align="center"><a href="https://github.com/CaoHoangTung"><img src="https://avatars.githubusercontent.com/u/22815550?v=4" width="100px;" alt=""/><br /><sub><b>Cao Hoang Tung</b></sub></a></td>
    <td align="center"><a href="https://github.com/ngocanhnckh"><img src="https://avatars.githubusercontent.com/u/12997699?v=4" width="100px;" alt=""/><br /><sub><b>Nguyen Ngoc Anh</b></sub></a></td>
    <td align="center"><a href="https://github.com/chpiano2000"><img src="https://avatars.githubusercontent.com/u/22815550?v=4" width="100px;" alt=""/><br /><sub><b>Vo Chi Dat</b></sub></a></td>
    <td align="center"><a href="https://github.com/rxng8"><img src="https://avatars.githubusercontent.com/u/60036798?v=4" width="100px;" alt=""/><br /><sub><b>Nguyen Viet Dung</b></sub></a></td>
    <td align="center"><a href="https://github.com/quangminhdinh"><img src="https://avatars.githubusercontent.com/u/31373940?v=4" width="100px;" alt=""/><br /><sub><b>Dinh Quang Minh</b></sub></a></td>
    <td align="center"><a href="https://github.com/duongdanghung20"><img src="https://avatars.githubusercontent.com/u/74593730?v=4" width="100px;" alt=""/><br /><sub><b>Duong Dang Hung</b></sub></a></td>
  </tr>
  <tr>
  </tr>
</table>

[contributors-shield]:https://img.shields.io/badge/CONTRIBUTORS-7-green?style=for-the-badge
[contributors-url]: https://github.com/aidenpearce001/Phishing-detection-ML/graphs/contributors
[forks-shield]: https://img.shields.io/badge/FORKS-2-blue?style=for-the-badge
[forks-url]: https://github.com/aidenpearce001/Phishing-detection-ML/network/members
[stars-shield]: https://img.shields.io/badge/STARS-2-blue?style=for-the-badge
[stars-url]: https://github.com/aidenpearce001/Phishing-detection-ML/stargazers
[organization-shield]: https://img.shields.io/badge/organization-YoungIT-lightgrey?style=for-the-badge&logo=appveyor
[organization-url]: https://www.facebook.com/youngit.org
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/aidenpearce001/Phishing-detection-ML/blob/main/LICENSE
[project-shield]: https://img.shields.io/badge/Project-chongluadao-green?style=for-the-badge&logo=appveyor
[project-url]: https://www.facebook.com/chongluadao.vn
[cld-home]: src/images/home.PNG
[cld-check]: src/images/check.PNG
[cld-dashhboard]: src/images/dashboard.PNG

