<script>
  export let files = [];

  let currentPage = 1;
  const pageSize = 5;

  function download(filename) {
  fetch(`http://localhost:5001/download/${encodeURIComponent(filename)}`)
    .then(res => {
      if (!res.ok) throw new Error('다운로드 실패');
      return res.blob();
    })
    .then(blob => {
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = filename;
      a.click();
      window.URL.revokeObjectURL(url);
    })
    .catch(err => {
      alert(`❌ 다운로드 실패: ${err.message}`);
    });
}



  async function retry(filename) {
  const confirmRetry = confirm(`${filename} 파일을 재처리 하시겠습니까?`);
  if (!confirmRetry) return;

  try {
    const res = await fetch('http://localhost:5001/retry', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ filename })
    });

    if (res.ok) {
      alert(`✅ ${filename} 재처리가 완료되었습니다.`);
    } else {
      const error = await res.json();
      alert(`❌ 실패: ${error.error}`);
      }
    } catch (err) {
      console.error('🚨 네트워크 오류:', err);
      alert('서버 연결 실패');
    }
  }


  // 페이지 계산
  $: totalPages = Math.ceil(files.length / pageSize);
  $: paginatedFiles = files.slice((currentPage - 1) * pageSize, currentPage * pageSize);

  function goToPage(page) {
    if (page >= 1 && page <= totalPages) {
      currentPage = page;
    }
  }
</script>

<div class="p-6 bg-white rounded-lg shadow mb-10 overflow-x-auto">
  <h3 class="mb-4 text-lg font-semibold">최근 업로드 파일</h3>
  <table class="w-full text-sm text-left text-gray-700 min-w-[600px]">
    <thead class="text-xs text-gray-500 uppercase bg-gray-50">
      <tr>
        <th class="px-4 py-2">파일명</th>
        <th class="px-4 py-2">작업유형</th>
        <th class="px-4 py-2">생성일</th>
        <th class="px-4 py-2">상태</th>
        <th class="px-4 py-2">작업</th>
      </tr>
    </thead>
    <tbody>
      {#each paginatedFiles as file}
        <tr class="border-t">
          <td class="px-4 py-2">{file.filename}</td>
          <td class="px-4 py-2">{file.type}</td>
          <td class="px-4 py-2">{file.date}</td>
          <td class="px-4 py-2">
            {#if file.status === '완료'}
              <span class="text-green-600 font-medium">완료</span>
            {:else}
              <span class="text-red-600 font-medium">실패</span>
            {/if}
          </td>
          <td class="px-4 py-2 space-x-2">
            <button class="text-blue-600 hover:underline" on:click={() => download(file.filename)}>다운로드</button>
            <button class="text-yellow-600 hover:underline" on:click={() => retry(file.filename)}>재시도</button>
          </td>
        </tr>
      {/each}
    </tbody>
  </table>

  <!-- 페이지네이션 (모바일 대응 포함) -->
  {#if totalPages > 1}
    <div class="flex flex-wrap justify-center mt-4 space-x-2 text-sm">
      <button class="px-2 py-1 border rounded disabled:opacity-50" on:click={() => goToPage(currentPage - 1)} disabled={currentPage === 1}>
        이전
      </button>

      {#each Array(totalPages) as _, i}
        <button
          class="px-2 py-1 border rounded {currentPage === i + 1 ? 'bg-blue-100 font-bold' : ''}"
          on:click={() => goToPage(i + 1)}
        >
          {i + 1}
        </button>
      {/each}

      <button class="px-2 py-1 border rounded disabled:opacity-50" on:click={() => goToPage(currentPage + 1)} disabled={currentPage === totalPages}>
        다음
      </button>
    </div>
  {/if}
</div>
