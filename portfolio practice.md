`20190829Th`

# 포트폴리오 만들기 연습

1. https://startbootstrap.com/themes/resume/
   - 형식 다운로드
   - https://fontawesome.com/ : 아이콘 class
2. open with Code -> bash terminal open
   - 수정 후
3. Github에 `<username>.github.io`형식으로새로운 repository 추가

3. 외부 저장소 origin에 `username.github.io` URL 추가

4. push

```bash
student@M5035 MINGW64 ~/Desktop/startbootstrap-resume-gh-pages (master)
$ git init
Reinitialized existing Git repository in C:/Users/student/Desktop/startbootstrap-resume-gh-pages/.git/

student@M5035 MINGW64 ~/Desktop/startbootstrap-resume-gh-pages (master)
$ git add .

student@M5035 MINGW64 ~/Desktop/startbootstrap-resume-gh-pages (master)
$ git remote add origin https://github.com/RubinYoon/RubinYoon.github.io.git
fatal: remote origin already exists.

student@M5035 MINGW64 ~/Desktop/startbootstrap-resume-gh-pages (master)
$ git push origin master
Username for 'https://github.com': RubinYoon
Password for 'https://RubinYoon@github.com':
Enumerating objects: 89, done.
Counting objects: 100% (89/89), done.
Delta compression using up to 4 threads
Compressing objects: 100% (87/87), done.
Writing objects: 100% (89/89), 1.90 MiB | 1.19 MiB/s, done.
Total 89 (delta 18), reused 0 (delta 0)
remote: Resolving deltas: 100% (18/18), done.
To https://github.com/RubinYoon/RubinYoon.github.io.git
 * [new branch]      master -> master
```

