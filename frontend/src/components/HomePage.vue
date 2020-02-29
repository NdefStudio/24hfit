<template>
  <div class='page'>
    <router-link to='login'
                 tag='p'
                 class='center_block'>{{Title}}</router-link>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
  data() {
    return {
      Title: '24hFit'
    }
  }
}
</script>

<style>
.page {
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.center_block {
  background-color: #f0f;
}
</style>