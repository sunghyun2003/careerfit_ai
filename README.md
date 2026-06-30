# careerfit_ai
> 취업·공모전 데이터 기반 맞춤형 AI 포트폴리오 코치

## 프로젝트 개요
취업을 희망하는 학부생을 위한 AI 개발

## 기술 스택
| 영역 | 기술 |
|---|---|
| 백엔드 | Python, FastAPI |
| AI API | Gemini 2.5 Flash-Lite |
| 데이터 | Pandas, SQLite, ChromaDB |
| 프론트엔드 | React, Vite |
| 실행 환경 | Docker |

## 진행 현황
- [x] 1일차: 프로젝트 기획 및 개발 환경 세팅
- [x] 2일차: FastAPI 서버 구축 및 Gemini API 연결
- [ ] 3일차: 데이터 파이프라인 구축
- [ ] 4일차: RAG 기반 서비스 + React UI
- [ ] 5일차: Docker + 포트폴리오 완성

## 🚀 2일차 진행 현황 (백엔드 기본 세팅 및 API 연동)
- Python 환경 구축: 가상환경(venv) 세팅 및 백엔드 필수 패키지 설치 완료
- FastAPI 서버 구축: 상태 확인(/health), 공고 조회(/jobs), AI 분석(/analyze) 핵심 엔드포인트 구현
- AI 모델 연동: Gemini 2.5 Flash-Lite API를 연결하여 맞춤형 분석 로직의 뼈대 완성
- 개발 환경 최적화: 원활한 테스트 및 프론트엔드 협업을 위한 Mock Mode 환경변수 적용