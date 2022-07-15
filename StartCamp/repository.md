#  1. 온라인 실습실

- 과제
- 온라인 제출
- 당일제출





# 2. 깃랩

-  pdf repo
- 그 주 금요일까지
- 월 HW - > 화 풀이
- 화 HW -> 화 풀이
- 수 HW -> 목 풀이                                                          
- 금 HW x



# 3.  Repository

- git init 명령어로 로컬 저장소 생성
- .git 디렉토리에 버전 관리에 필요한 모든 것이 다 있음





# 4. git 기본

- README.md 생성하기
- working directory : 작업중 디렉토리
- staging area : 커밋으로 남기고싶은 특정 버전파일이 존재하는곳 
- repository : 커밋들이 저장되는곳
- untracked(working directory) -> git add -> tracked, staged(staging area) -> git commit -> tracked, committed(repository)
- git config --global user.email {email}
- git config --global user.name {name}
- git add(파일명 or 위치) - 파일들을 스테이지 위로 올림
- git commit -m ""  >>>>> 순서대로 git modified 쌓임 
- git remote add origin {URL} >> 원격 저장소를 origin 이라는 이름으로 add함
- git push -u origin master >> master가 commit 한 결과들 origin이라는 원격저장소 깃허브로 전송
- git status, git log, 
- git log --oneline
- git clone >> 최초로 컴퓨터로 깃 내용물을 가져올때
- git pull origin master >> master에게 origin을 내보내기