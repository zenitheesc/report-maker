from pylatex import Document, Section, Subsection, Command
from pylatex.utils import italic, NoEscape
from pylatex.package import Package
import datetime
from zipfile import ZipFile
import os
from os.path import basename

now = datetime.datetime.now()


titulo = "Título de meu arquivo"
resumo = "Resumo de meu arquivo"
conteudo = "Conteúdo de meu arquivo"
conclusao = "Conclusão de meu arquivo"

filepath = (r"latex_generator\output")
doc = Document(filepath)
doc.documentclass = Command(
        'documentclass',
        options=['brazilian', '12pt', 'oneside', 'a4paper'],
        arguments=['article'],
    )

doc.preamble.append(NoEscape(r'\input{preamble.tex}'))
doc.preamble.append(Command('titulo', {titulo}))
doc.preamble.append(NoEscape(r'\data{\today}'))
doc.append(NoEscape(r'\setFaixa'))
doc.append(NoEscape(r'\geraTitulo'))
doc.append(NoEscape(r'\section{Resumo}'))
doc.append(resumo)
doc.append(NoEscape(r'\section{Conteúdo}'))
doc.append(conteudo)
doc.append(NoEscape(r'\section{Conclusão}'))
doc.append(conclusao)
doc.append(NoEscape(r'\section{Dados}'))
#aqui adicionar as imagens
#doc.append(NoEscape(r"""
#\begin{figure}
#\begin{tabular}{cccc}
#\subfloat[caption]{\includegraphics[width = 1.5in]{something}} &
#\subfloat[caption]{\includegraphics[width = 1.5in]{something}} &
#\subfloat[caption]{\includegraphics[width = 1.5in]{something}} &
#\subfloat[caption]{\includegraphics[width = 1.5in]{something}}\\
#\subfloat[caption]{\includegraphics[width = 1.5in]{something}} &
#\subfloat[caption]{\includegraphics[width = 1.5in]{something}} &
#\subfloat[caption]{\includegraphics[width = 1.5in]{something}} &
#\subfloat[caption]{\includegraphics[width = 1.5in]{something}}\\
#\subfloat[caption]{\includegraphics[width = 1.5in]{something}} &
#\subfloat[caption]{\includegraphics[width = 1.5in]{something}} &
#\subfloat[caption]{\includegraphics[width = 1.5in]{something}} &
#\subfloat[caption]{\includegraphics[width = 1.5in]{something}}\\
#\subfloat[caption]{\includegraphics[width = 1.5in]{something}} &
#\subfloat[caption]{\includegraphics[width = 1.5in]{something}} &
#\subfloat[caption]{\includegraphics[width = 1.5in]{something}} &
#\subfloat[caption]{\includegraphics[width = 1.5in]{something}}
#\end{tabular}
#\caption{4 x 4}
#\end{figure}
#"""))

filename=(r"\zenith_report_{dia}-{mes}-{ano}".format(dia=now.day, mes=now.month, ano=now.year))
doc.generate_tex(r"{filepath}{filename}".format(filepath=filepath, filename=filename))

#creating the zipfile

with ZipFile("zenith_report_{dia}-{mes}-{ano}.zip".format(dia=now.day, mes=now.month, ano=now.year), "w") as zipObj:
   # Iterate over all the files in directory
   for folderName, subfolders, filenames in os.walk(r"latex_generator\output"):
       for filename in filenames:
           #create complete filepath of file in directory
           filePath = os.path.join(folderName, filename)
           # Add file to zip
           zipObj.write(filePath, basename(filePath))