<script>
  let selectedFile = null;
  let errorMessage = '';
  const allowedExtensions = ['pdf', 'docx', 'txt', 'csv'];

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
    // 👉 여기서 백엔드 업로드 로직 추가 가능
  }

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
</script>

<div class="p-6 space-y-4 bg-white rounded-lg shadow">
  <h3 class="text-lg font-semibold">컴포넌트 타이틀</h3>
  <p class="text-sm text-gray-600">
    요약 설명
  </p>

  <!-- 업로드 영역 -->
  <div
    class="p-6 text-sm text-center text-gray-500 border-2 border-dashed rounded cursor-pointer hover:bg-gray-50"
    on:drop={onDrop}
    on:dragover={onDragOver}
  >
    <label for="file-upload" class="cursor-pointer">
      파일을 이곳에 끌어다 놓거나 <span class="font-semibold text-blue-600">파일 선택</span>
    </label>
    <input id="file-upload" type="file" accept=".pdf,.docx,.txt,.csv" class="hidden" on:change={onFileChange} />
  </div>

  <!-- 확장자 안내 -->
  <div class="flex gap-2 text-xs text-gray-500">
    <span class="px-2 py-1 border rounded">PDF</span>
    <span class="px-2 py-1 border rounded">DOCX</span>
    <span class="px-2 py-1 border rounded">TXT</span>
    <span class="px-2 py-1 border rounded">CSV</span>
  </div>

  <!-- 상태 표시 -->
  {#if selectedFile}
    <p class="text-sm text-green-600">✅ {selectedFile.name} 업로드 준비 완료</p>
  {/if}

  {#if errorMessage}
    <p class="text-sm text-red-600">⚠️ {errorMessage}</p>
  {/if}
</div>
