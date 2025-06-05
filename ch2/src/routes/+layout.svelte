<script>
import "../app.css";
import Header from '$lib/Header.svelte';
import Sidebar from '$lib/Sidebar.svelte';
</script>

<div class="flex flex-col h-screen">
  <Header></Header>
  <div class="flex flex-1 overflow-hidden">
    <Sidebar></Sidebar>
    <main class="flex-1 p-6 overflow-y-auto bg-gray-50">
      <slot></slot>
    </main>
  </div>
</div>
