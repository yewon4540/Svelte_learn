<script>
  import ToolCard1 from '$lib/ToolCard.svelte';
  import ToolCard2 from '$lib/ToolCard.svelte';
  import RecentTable from '$lib/RecentTable.svelte';
  import Stats from '$lib/Stats.svelte';
  import { onMount } from 'svelte';

  let recentFiles = [];

  onMount(async () => {
    try {
      const res = await fetch('http://localhost:5001/api/files');
      const data = await res.json();
      recentFiles = data;
    } catch (err) {
      console.error('❌ 최근 파일 목록을 불러오는 데 실패했습니다.', err);
    }
  });
</script>

<h2 class="mb-6 text-2xl font-bold">Sub Title</h2>

<div class="grid grid-cols-1 gap-6 mb-10 md:grid-cols-2">
  <ToolCard1
    title="긍정 사전"
    description="긍정 사전 만들기"
    uploadDir='happy'
  />
  <ToolCard2
    title="부정 사전"
    description="부정 사전 만들기"
    uploadDir='ohno'
  />
</div>

<RecentTable files={recentFiles} />
<Stats />
