<template>
  <div class="page">
    <router-link to="login"
                 tag="div"
                 class="center_block">
      <img class='coverimg'
           src="/static/img/导入页4.png">
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'CoverPage',
  data() {
    return {
      Title: '24hFit'
    }
  },
  mounted() {
    var that = this
    setTimeout(function() {
      console.log('go')
      that.$router.push({ path: '/login' })
    }, 2000)
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
  display: flex;
  justify-content: center;
  align-items: center;
}
.coverimg {
  width: auto;
  height: auto;
  max-width: 100%;
  max-height: 100%;
}
</style>