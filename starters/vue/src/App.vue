<script setup>
// The brand's files are in public/brand/; BASE_URL keeps them reachable
// under any path.
const brand = `${import.meta.env.BASE_URL}brand`;
const cards = [
  { for: "Colours", name: "tokens.css", note: "--rs-* variables follow light and dark." },
  { for: "Logo, icons", name: "brand/", note: "All rights reserved: our own pages only." },
  { for: "Deploy", name: "GitHub Pages", note: "A push to master publishes the site." },
];
</script>

<template>
  <main>
    <img class="brand" :src="`${brand}/images/logo/mark.svg`" alt="RedScope Technologies" />
    <h1>RedScope Technologies</h1>
    <p class="muted">A Vue starter in the RedScope style. Replace this page with your own.</p>
    <h2>What is here</h2>
    <div class="grid">
      <div v-for="card in cards" :key="card.for" class="card">
        <div class="for">{{ card.for }}</div>
        <div class="name">{{ card.name }}</div>
        <div class="note">{{ card.note }}</div>
      </div>
    </div>
    <footer class="muted">© RedScope Technologies</footer>
  </main>
</template>
