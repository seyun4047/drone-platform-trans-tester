echo "해당 문서는 gemini-2.5-flash 로 자동 번역되었습니다.<br>정확한 내용은 여기서 확인해주세요: [English Document](https://github.com/seyun4047/drone-platform-trans-tester/blob/main/README.md)" > README.kr.md
echo -e "\n---\n" >> README.kr.md
if [ -f components/trans-tester/trans-tester.kr.md ]; then
    cat components/trans-tester/trans-tester.kr.md >> README.kr.md
fi
echo -e "\n\n---\n" >> README.kr.md
if [ -f components/platform/overview.kr.md ]; then
    cat components/platform/overview.kr.md >> README.kr.md
fi
