<h1 align="center" style="color:white; background-color:black">Report Maker</h1>
<h4 align="center">An automation tool designed to make the report production easier due to the automatization of the space log parsing and graphic generation   </h4>

<p align="center">
	<a href="http://zenith.eesc.usp.br/">
    <img src="https://img.shields.io/badge/Zenith-Embarcados-black?style=for-the-badge"/>
    </a>
    <a href="https://eesc.usp.br/">
    <img src="https://img.shields.io/badge/Linked%20to-EESC--USP-black?style=for-the-badge"/>
    </a>
    <a href="https://github.com/zenitheesc/Report_Maker/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/zenitheesc/Report_Maker?style=for-the-badge"/>
    </a>
    <a href="https://github.com/zenitheesc/Report_Maker/issues">
    <img src="https://img.shields.io/github/issues/zenitheesc/Report_Maker?style=for-the-badge"/>
    </a>
    <a href="https://github.com/zenitheesc/Report_Maker/commits/main">
    <img src="https://img.shields.io/github/commit-activity/m/zenitheesc/Report_Maker?style=for-the-badge">
    </a>
    <a href="https://github.com/zenitheesc/Report_Maker/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/zenitheesc/Report_Maker?style=for-the-badge"/>
    </a>
    <a href="https://github.com/zenitheesc/Report_Maker/commits/main">
    <img src="https://img.shields.io/github/last-commit/zenitheesc/Report_Maker?style=for-the-badge"/>
    </a>
    <a href="https://github.com/zenitheesc/Report_Maker/issues">
    <img src="https://img.shields.io/github/issues-raw/zenitheesc/Report_Maker?style=for-the-badge" />
    </a>
    <a href="https://github.com/zenitheesc/Report_Maker/pulls">
    <img src = "https://img.shields.io/github/issues-pr-raw/zenitheesc/Report_Maker?style=for-the-badge">
    </a>
</p>

<p align="center">
    <a href="#environment-and-tools">Environment and Tools</a> •
    <a href="#steps-to-run-and-debug">Steps to run and debug</a> •
    <a href="#how-to-contribute">How to contribute?</a>
</p>

## Environment and tools

In this project, our three main goals were:
1. Create a versatile and modular parser dedicate to parse any Zenith Aerospace log;
2. Generate charts based on the data and eliminate outliers;
3. Generate a LaTeX report with the data provided by the parser.

Moreover, all these goals should've been achieved in a user-friendly GUI. 

Due to the versatility, we picked **Python** as your primary development language. Report Maker's parser was developed using regular expression (**RegEx**) knowledge. The statistics stage was developed with famous **data science** libraries such as Pandas, Matplotlib, and Numpy. This stage also made it possible to generate maps when the log has geographic coordinates. At last, the pylatex library was used to generate a **LaTeX** file. 
As many Report Maker's users are not programmers, we built a GUI with a Pyhton native module, **Tkinter**.

<div align='center'> 
    <img src='Report Maker.png' width='80%'/>
</div>

## Steps to run and debug

First of all, you must have [python3](/www.python.org/downloads/) (with pip) installed. With you have already completed this requirement, then run the following command in the terminal:

```
git clone https://github.com/zenitheesc/Report_Maker.git
```

If you're using a **Windows** machine, just click on **Run.bat** and you should be good to go. But, if you're using **Linux/OSX** machine or a **virtual environment** such as conda, then run the following commands in the terminal:

```
python3 -m pip install -r requirements.txt
python3 main.py
```

## How to contribute

We love when new people come and help us to improve our software! If you want to contribute to this project, check our Projects board and pick an idea to develop. When you finish coding, make a clear and descriptive **pull request** explaining your modifications. 

If you find any sort of problem or have a suggestion to the project, please write an **issue** and we will be pleased to help you!

### Developers

| [<img src="https://github.com/jorgemrisco.png?size=115" width=115><br><sub>@jorgemrisco</sub>](https://github.com/jorgemrico) | [<img src="https://github.com/leocelente.png?size=115" width=115><br><sub>@leocelente</sub>](https://github.com/leocelente) | [<img src="https://github.com/mairacanal.png?size=115" width=115><br><sub>@mairacanal</sub>](https://github.com/mairacanal)
| :---: | :---: | :---: |
---

<p align="center">
    <a href="http://zenith.eesc.usp.br">
    <img src="https://img.shields.io/badge/Check%20out-Zenith's Oficial Website-black?style=for-the-badge" />
    </a> 
    <a href="https://www.facebook.com/zenitheesc">
    <img src="https://img.shields.io/badge/Like%20us%20on-facebook-blue?style=for-the-badge"/>
    </a> 
    <a href="https://www.instagram.com/zenith_eesc/">
    <img src="https://img.shields.io/badge/Follow%20us%20on-Instagram-red?style=for-the-badge"/>
    </a>

</p>
<p align = "center">
<a href="zenith.eesc@gmail.com">zenith.eesc@gmail.com</a>
</p>
