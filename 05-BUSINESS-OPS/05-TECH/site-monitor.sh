#!/bin/bash
# LMT Site Monitor — checks key pages for broken elements
# Run: bash ~/Desktop/LMT-CONTENT/06-ASSETS/site-monitor.sh

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'
FAIL=0

echo "========================================="
echo " LMT SITE MONITOR — $(date '+%Y-%m-%d %I:%M %p')"
echo "========================================="

# --- Programs Page ---
echo ""
echo ">> Programs Page (/programs/)"
PROG=$(curl -s "https://learnmoretechnologies.com/programs/" 2>/dev/null)
PROG_STATUS=$(curl -s -o /dev/null -w "%{http_code}" "https://learnmoretechnologies.com/programs/" 2>/dev/null)

if [ "$PROG_STATUS" != "200" ]; then
  echo -e "${RED}DOWN — HTTP $PROG_STATUS${NC}"
  FAIL=1
else
  echo -e "${GREEN}UP — HTTP 200${NC}"
fi

# Check 3 YouTube iframes
IFRAME_COUNT=$(echo "$PROG" | grep -c "youtube.com/embed")
if [ "$IFRAME_COUNT" -ge 3 ]; then
  echo -e "${GREEN}Videos: $IFRAME_COUNT YouTube iframes found${NC}"
else
  echo -e "${RED}BROKEN — Only $IFRAME_COUNT of 3 YouTube iframes found${NC}"
  FAIL=1
fi

# Check for BuddyBoss max-width override killing layout
BB_OVERRIDE=$(echo "$PROG" | grep -c 'entry-content.*max-width:860px')
if [ "$BB_OVERRIDE" -gt 0 ]; then
  echo -e "${YELLOW}WARNING — BuddyBoss max-width:860px override detected (videos may be hidden)${NC}"
  FAIL=1
fi

# Check prog-video containers exist
PV_COUNT=$(echo "$PROG" | grep -c "prog-video")
if [ "$PV_COUNT" -ge 6 ]; then
  echo -e "${GREEN}Layout: prog-video containers present${NC}"
else
  echo -e "${RED}BROKEN — prog-video containers missing ($PV_COUNT found, need 6+)${NC}"
  FAIL=1
fi

# --- Homepage ---
echo ""
echo ">> Homepage"
HOME_STATUS=$(curl -s -o /dev/null -w "%{http_code}" "https://learnmoretechnologies.com/" 2>/dev/null)
if [ "$HOME_STATUS" != "200" ]; then
  echo -e "${RED}DOWN — HTTP $HOME_STATUS${NC}"
  FAIL=1
else
  echo -e "${GREEN}UP — HTTP 200${NC}"
fi

# --- Course Page ---
echo ""
echo ">> Course Page (/courses/50techbridge/)"
COURSE_STATUS=$(curl -s -o /dev/null -w "%{http_code}" "https://learnmoretechnologies.com/courses/50techbridge/" 2>/dev/null)
if [ "$COURSE_STATUS" != "200" ]; then
  echo -e "${RED}DOWN — HTTP $COURSE_STATUS${NC}"
  FAIL=1
else
  echo -e "${GREEN}UP — HTTP 200${NC}"
fi

# --- Lessons ---
echo ""
echo ">> Lessons"
for LESSON in "introduction-to-digital-skills-agetech" "using-mobile-devices-accessing-online-services" "technology-for-independent-living"; do
  L_STATUS=$(curl -s -o /dev/null -w "%{http_code}" "https://learnmoretechnologies.com/courses/50techbridge/lessons/$LESSON/" 2>/dev/null)
  if [ "$L_STATUS" != "200" ]; then
    echo -e "${RED}DOWN — $LESSON (HTTP $L_STATUS)${NC}"
    FAIL=1
  else
    echo -e "${GREEN}UP — $LESSON${NC}"
  fi
done

# --- Work With Brian ---
echo ""
echo ">> Work With Brian"
WWB_STATUS=$(curl -s -o /dev/null -w "%{http_code}" "https://learnmoretechnologies.com/work-with-brian/" 2>/dev/null)
if [ "$WWB_STATUS" != "200" ]; then
  echo -e "${RED}DOWN — HTTP $WWB_STATUS${NC}"
  FAIL=1
else
  echo -e "${GREEN}UP — HTTP 200${NC}"
fi

# --- Summary ---
echo ""
echo "========================================="
if [ "$FAIL" -eq 0 ]; then
  echo -e "${GREEN}ALL CLEAR — No issues detected${NC}"
else
  echo -e "${RED}ISSUES FOUND — Check above${NC}"
fi
echo "========================================="
