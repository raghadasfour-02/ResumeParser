# Raghad's Resume Parser 
A resume parser to see how well your resume is read by Application Tracking Systems (ATS)

---
### Inspiration 
Upon learning that companies use an ATS to process our resumes, I was inspired to create a system that replicates the behaviour of an ATS. This would allow co-op students at the University of Waterloo to adjust their stylistic choices on their resume. 
### What did I learn? [ABOUT PROGRAMMING]
- Parsing .pdf and/or .docx files
- Setting up an efficient way to extract information from parsed data
- Utilizing Django's Framework to setup a Resume Parser Admin
- Configuring 'views' to accept resume for parsing and notify user of duplicate uploads
### What did I learn? [ABOUT WRITING SOFTWARE]
- How to write short, concise functions that serve one purpose only
- When choosing to divide methods, divide based on purpose rather than behaviour. This allowed me to further expand on methods without the need to conduct major refactoring. For example, the extraction of name and university name may appear to be identical in behaviour at first. Though it was tempting to create one method to extract both full name and university name, I learned otherwise. The two tasks must be divided to two different methods to account for possible future changes. I learned that a good rule of thumb is to divide methods based on purpose. 