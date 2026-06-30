# prompt_manager.py — AI 프롬프트 관리 프로그램


# 프롬프트를 담는 리스트. 딕셔너리 하나 = 프롬프트 하나.
prompts = [
    {
        "title": "블로그 글 작성",
        "content": "다음 주제로 블로그 글을 써줘. 제목, 소제목, 본문 순서로 구성하고 2000자 내외로 작성해.",
        "category": "텍스트 생성",
        "favorite": False,
    },
    {
        "title": "수채화풍 풍경 이미지",
        "content": "A serene mountain landscape at sunset, watercolor style, soft pastel colors, highly detailed, 4K.",
        "category": "이미지 생성",
        "favorite": True,
    },
    {
        "title": "친절한 고객 상담 페르소나",
        "content": "너는 10년 경력의 고객 상담 전문가야. 항상 공감하는 말투로 답하고, 문제 해결을 최우선으로 해.",
        "category": "페르소나",
        "favorite": False,
    },
]


def show_menu():
    # 사용자에게 선택지를 보여주는 함수
    print("\n===== AI 프롬프트 관리자 =====")
    print("1. 프롬프트 추가")
    print("2. 전체 목록 보기")
    print("3. 카테고리별 조회")
    print("4. 검색")
    print("5. 상세 보기")
    print("6. 즐겨찾기 관리")
    print("0. 종료")
    print("==============================")


def add_prompt():
    # 메뉴 1번: 프롬프트 추가 (아직 미구현)
    print("\n[프롬프트 추가] — 아직 준비 중입니다.")


def show_all():
    # 메뉴 2번: 전체 목록 보기 (아직 미구현)
    print("\n[전체 목록 보기] — 아직 준비 중입니다.")


def show_by_category():
    # 메뉴 3번: 카테고리별 조회 (아직 미구현)
    print("\n[카테고리별 조회] — 아직 준비 중입니다.")


def search_prompt():
    # 메뉴 4번: 검색 (아직 미구현)
    print("\n[검색] — 아직 준비 중입니다.")


def show_detail():
    # 메뉴 5번: 상세 보기 (아직 미구현)
    print("\n[상세 보기] — 아직 준비 중입니다.")


def manage_favorite():
    # 메뉴 6번: 즐겨찾기 관리 (아직 미구현)
    print("\n[즐겨찾기 관리] — 아직 준비 중입니다.")


def run():
    # 프로그램의 메인 루프
    # 메뉴를 보여주고 → 번호를 받고 → 해당 기능 실행 → 다시 메뉴로
    print("AI 프롬프트 관리자를 시작합니다.")

    while True:
        show_menu()
        choice = input("번호를 입력하세요: ").strip()

        if choice == "1":
            add_prompt()
        elif choice == "2":
            show_all()
        elif choice == "3":
            show_by_category()
        elif choice == "4":
            search_prompt()
        elif choice == "5":
            show_detail()
        elif choice == "6":
            manage_favorite()
        elif choice == "0":
            print("\n프로그램을 종료합니다. 안녕히 가세요!")
            break
        else:
            # 목록에 없는 번호를 입력했을 때
            print("\n올바르지 않은 번호입니다. 다시 선택해 주세요.")


# 이 파일을 직접 실행할 때만 run()을 호출한다
if __name__ == "__main__":
    run()
