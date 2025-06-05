from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import psycopg2
import requests
import os

DB_CONFIG = {
    'host': 'localhost',
    'port': '5432',
    'dbname': 'yewon',
    'user': 'yewon',     # 실제 사용자 이름으로 변경
    'password': 'yewon'  # 실제 비밀번호로 변경
}

# postgre에 사전정보 업로드
def insert_uploaded_file(filename, filetype, status="완료"):
    print("🔘 ȸ 접속 중 🔘")
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO uploaded_files (filename, type, date, status)
        VALUES (%s, %s, CURRENT_DATE, %s)
    """, (filename, filetype, status))

    print("🔘 DB 데이터 입력 완료 🔘")
    conn.commit()
    cur.close()
    conn.close()

# 재귀 요청을 위한 함수
def process_synonym_file(filename, upload_dir, generate_title): # 일단 컴포넌트 타이틀은 가져와보기
    input_path = os.path.join('data', upload_dir, filename)
    output_dir = os.path.join('data', f'out_{upload_dir}')
    
    pre_ = 'syn' if upload_dir == 'synonym' else 'neo'
    os.makedirs(output_dir, exist_ok=True)
    
    base_name, _ = os.path.splitext(filename)
    output_filename = f"{pre_}_{base_name}.csv"
    output_path = os.path.join(output_dir, output_filename)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("origin,synonym\ncar,boongboong\ndog,meongmoeng\n")

    # DB에 업로드 및 사전생성 기록 저장
    insert_uploaded_file(
        # filename=output_filename, # 사전 생성 후 파일 집어넣기
        filename,
        filetype=f"{generate_title} 사전 생성",
        status="완료"
    )

    print(f"✅ 생성된 파일: {output_path}")
    return {
        "message": "파일 생성 완료",
        "output_file": output_filename
    }


app = Flask(__name__)
CORS(app)

# 파일 업로드
@app.route('/upload', methods=['POST'])
def upload_file_real():
    uploaded_file = request.files.get('file')
    upload_dir = request.form.get('uploadDir', '')
    generate_title = request.form.get('title')

    if uploaded_file and upload_dir:
        os.makedirs(f"./data/{upload_dir}", exist_ok=True)
        filepath = f"./data/{upload_dir}/{uploaded_file.filename}"
        uploaded_file.save(filepath)

        result = process_synonym_file(uploaded_file.filename, upload_dir, generate_title)

        return jsonify({
            "message": f"{upload_dir}에 파일 저장 완료",
            "generate_status": result
            }), 201

    return jsonify({"error": "파일 또는 디렉토리 정보가 없습니다"}), 400


# DB에서 업로드 기록 조회
@app.route('/api/files', methods=['GET'])
def get_files():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("SELECT filename, type, date, status FROM uploaded_files ORDER BY id DESC")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    result = []
    for row in rows:
        result.append({
            "filename": row[0],
            "type": row[1],
            "date": row[2].strftime('%Y-%m-%d'),
            "status": row[3]
        })
    return jsonify(result)

# 서버 시작
if __name__ == '__main__':
    app.run(debug=True, port=5000)

