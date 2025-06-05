## 목적:
- 사용자가 PDF, DOCX, TXT, CSV 파일을 업로드
- 선택 또는 드래그 앤 드롭으로 파일 업로드 가능
- 허용된 확장자만 통과
- 업로드 상태와 에러 메시지 표시

## 1. 변수 선언
```
let selectedFile = null;
let errorMessage = '';
const allowedExtensions = ['pdf', 'docx', 'txt', 'csv'];
```
- selectedFile: 업로드된 파일 객체 저장
- errorMessage: 사용자에게 보여줄 에러 메시지
- allowedExtensions: 유효한 확장자 리스트

## 2. handleFileUpload(file)
```
function handleFileUpload(file) {
  const ext = file.name.split('.').pop().toLowerCase();
  if (!allowedExtensions.includes(ext)) {
    errorMessage = `허용되지 않은 파일 형식입니다: ${ext}`;
    selectedFile = null;
    return;
  }
  errorMessage = '';
  selectedFile = file;
  console.log('업로드된 파일:', file.name);
}
```
- 파일 확장자 분리 → 검증
- 에러 메시지 출력
- 유효한 경우 콘솔 로그

## 3. 파일 입력/드롭 이벤트 처리
```
function onFileChange(event) {
  const file = event.target.files[0];
  if (file) handleFileUpload(file);
}
function onDrop(event) {
  event.preventDefault();
  const file = event.dataTransfer.files[0];
  if (file) handleFileUpload(file);
}
function onDragOver(event) {
  event.preventDefault();
}
```
- drag & drop과 input 둘 다 지원
- 드래그 이벤트 기본 동작 제거

## 4. 템플릿 구조

### 업로드 영역
```
<div on:drop on:dragover>
  <label for="file-upload">파일 선택</label>
  <input type="file" class="hidden" />
</div>
```
- label + input[type=file] 조합: 접근성 좋음
- accept=".pdf,.docx,.txt,.csv": 브라우저 파일 다이얼로그에서도 필터 적용됨

## 5. 상태 UI
```
{#if selectedFile}
  <p>✅ {selectedFile.name} 업로드 준비 완료</p>
{/if}
{#if errorMessage}
  <p>⚠️ {errorMessage}</p>
{/if}
```
- 실시간 상태 반영
- 성공/실패에 따라 시각적 피드백 제공