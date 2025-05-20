<script>
  import ToolCard from '$lib/ToolCard.svelte';
  import RecentTable from '$lib/RecentTable.svelte';
  import Stats from '$lib/Stats.svelte';
</script>

<h2 class="mb-6 text-2xl font-bold">Sub Title</h2>

<div class="grid grid-cols-1 gap-6 mb-10 md:grid-cols-2">
  <ToolCard
    title="Comp1"
    description="description1"
  />
  <ToolCard
    title="Comp2"
    description="description2"
  />
</div>

<RecentTable />
<Stats />
