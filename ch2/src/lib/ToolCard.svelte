<script>
  console.log("ToolCard.svelte 실행");
  export let title;
  export let description;
  export let uploadDir = '';

  import { createEventDispatcher } from 'svelte';
  const dispatch = createEventDispatcher();

  const allowedExtensions = ['pdf', 'docx', 'txt', 'csv'];

  let selectedFile = null;
  let errorMessage = '';
  const inputId = `file-upload-${title}`;

  async function sendToBackend(file) {
    const formData = new FormData();
    formData.append('file', file);
    formData.append('uploadDir', uploadDir);
    formData.append('title', title);

    console.log(`[${title}] sendToBackend 실행됨`);

    try {
      const res = await fetch('http://127.0.0.1:5001/upload', {
        method: 'POST',
        body: formData
      });

      if (res.ok) {
        console.log('✅ 파일 업로드 성공');
        dispatch('uploaded'); // ✅ 상위 컴포넌트에 이벤트 전달
      } else {
        console.error('❌ 파일 업로드 실패 - 상태 코드:', res.status);
      }
    } catch (err) {
      console.error('🚨 fetch 오류 발생:', err);
    }
  }

  function handleFileUpload(file) {
    const ext = file.name.split('.').pop().toLowerCase();
    console.log(`[${title}] handleFileUpload 실행됨`);
    if (!allowedExtensions.includes(ext)) {
      errorMessage = `허용되지 않은 파일 형식입니다: ${ext}`;
      selectedFile = null;
      return;
    }
    errorMessage = '';
    selectedFile = file;
    console.log('업로드된 파일:', file.name);

    sendToBackend(file);
  }

  function onFileChange(event) {
    const file = event.target.files[0];
    console.log(`[${title}] onFileChange 실행됨`);
    if (file) handleFileUpload(file);
  }

  function onDrop(event) {
    console.log(`[${title}] onDrop 실행됨`);
    const file = event.dataTransfer.files[0];
    if (file) handleFileUpload(file);
  }

  function onDragOver(event) {
    console.log(`[${title}] onDragOver 실행됨`);
  }
</script>

<div class="p-6 space-y-4 bg-white rounded-lg shadow">
  <h3 class="text-lg font-semibold">{title}</h3>
  <p class="text-sm text-gray-600">
    {description}
  </p>

  <div
    role="button"
    tabindex="0"
    class="p-6 text-sm text-center text-gray-500 border-2 border-dashed rounded cursor-pointer hover:bg-gray-50"
    on:drop={onDrop}
    on:dragover={onDragOver}
  >
    <label for={inputId} class="cursor-pointer">
      파일을 이곳에 끌어다 놓거나 <span class="font-semibold text-blue-600">파일 선택</span>
    </label>
    <input
      id={inputId}
      type="file"
      accept=".pdf,.docx,.txt,.csv"
      class="hidden"
      on:change={onFileChange}
    />
  </div>

  <div class="flex gap-2 text-xs text-gray-500">
    <span class="px-2 py-1 border rounded">PDF</span>
    <span class="px-2 py-1 border rounded">DOCX</span>
    <span class="px-2 py-1 border rounded">TXT</span>
    <span class="px-2 py-1 border rounded">CSV</span>
  </div>

  {#if selectedFile}
    <p class="text-sm text-green-600">✅ {selectedFile.name} 업로드 완료!✌️</p>
    <p class="text-xs text-gray-400">🔍 title: {title}</p>
  {/if}

  {#if errorMessage}
    <p class="text-sm text-red-600">⚠️ {errorMessage}</p>
    <p class="text-xs text-gray-400">🔍 title: {title}</p>
  {/if}
</div>
