FROM python:3.7
#Copy forcepoint project
COPY . /Forcepoint Project/
#Run script
CMD [ "python", "./ForcepointScript.py" ]