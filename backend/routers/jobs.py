from fastapi import APIRouter
from typing import List
router = APIRouter()

# 목업 데이터: 3일차에 실제 CSV 데이터로 교체한다
MOCK_JOBS = [
    {
        "id": 1,
        "company": "테크스타트업A",
        "title": "데이터 분석가",
        "required_skills": ["Python", "SQL", "통계"],
        "preferred_skills": ["R", "Tableau", "머신러닝"],
        "description": "사용자 행동 데이터를 분석해 비즈니스 인사이트를 도출합니다.",
        "deadline": "2026-07-31"
    },

    {
        "id": 2,
        "company": "금융서비스B",
        "title": "백엔드 개발자",
        "required_skills": ["Python", "FastAPI", "PostgreSQL"],
        "preferred_skills": ["Docker", "AWS", "Redis"],
        "description": "금융 데이터 처리 API 서버를 개발하고 운영합니다.",
        "deadline": "2026-08-15"
    },

    {
        "id": 3,
        "company": "공공기관C",
        "title": "AI 연구원",
        "required_skills": ["Python", "딥러닝", "PyTorch"],
        "preferred_skills": ["논문 작성", "NLP", "컴퓨터 비전"],
        "description": "공공 서비스 개선을 위한 AI 모델을 연구·개발합니다.",
        "deadline": "2026-08-01"
    },

    {
        "id": 4,
        "company": "롯데케미칼",
        "title": "공정엔지니어",
        "required_skills": ["화학공학 전공지식(반응공학·단위조작)", "Aspen HYSYS", "P&ID 해석"],
        "preferred_skills": ["공정안전관리(PSM)", "화학공학기사"],
        "description": "석유화학 플랜트의 생산 공정을 모니터링하고 수율과 에너지 효율을 개선합니다. 공정 데이터를 분석해 트러블슈팅과 운전 조건 최적화를 수행합니다.",
        "deadline": "2026-08-31"
    },

    {
        "id": 5,
        "company": "LG에너지솔루션",
        "title": "이차전지 소재 연구원",
        "required_skills": ["전기화학", "재료 분석(XRD·SEM)", "실험설계(DOE)"],
        "preferred_skills": ["Python 데이터 분석", "비즈니스 영어"],
        "description": "차세대 이차전지용 양극재 소재를 합성하고 전기화학 특성을 평가합니다. 실험 데이터를 기반으로 소재 조성과 공정 조건을 최적화합니다.",
        "deadline": "2026-08-31"
    },

    {
        "id": 6,
        "company": "한화솔루션",
        "title": "품질관리 엔지니어",
        "required_skills": ["통계적 공정관리(SPC)", "Minitab", "품질경영(ISO 9001)"],
        "preferred_skills": ["식스시그마(Six Sigma)", "HAZOP"],
        "description": "화학 제품 생산 라인의 품질 지표를 관리하고 불량 원인을 분석해 개선합니다. SPC 기반으로 공정 변동을 모니터링하며 품질 시스템을 운영합니다.",
        "deadline": "2026-08-31"
    }

]

@router.get("/jobs", tags=["Jobs"])
def get_jobs():
    """
    취업 공고 목록을 반환하는 엔드포인트.
    현재는 목업 데이터를 반환하며, 3일차에 실제 데이터로 교체한다.
    """
    return {
        "count": len(MOCK_JOBS),
        "jobs": MOCK_JOBS
    }

@router.get("/jobs/{job_id}", tags=["Jobs"])
def get_job_by_id(job_id: int):
    """
    특정 공고의 상세 정보를 반환한다.
    """
    for job in MOCK_JOBS:
        if job["id"] == job_id:
            return job
    # 찾지 못한 경우
    from fastapi import HTTPException
    raise HTTPException(status_code=404, detail=f"공고 ID {job_id}를 찾을 수 없습니다.")