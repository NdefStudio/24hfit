<template>
  <div class="page">
    <router-link to="cover"
                 tag="div"
                 class="center_block">
      <img class="coverimg"
           :src="img">
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
  data() {
    return {
      Title: '24hFit',
      img: ''
    }
  },
  mounted() {
    var that = this
    var hh = new Date().getHours()
    if (hh < 9 && hh > 4) {
      that.img = '/static/img/导入页1.png'
    } else if (hh >= 9 && hh < 19) {
      that.img = '/static/img/导入页2.png'
    } else that.img = '/static/img/导入页3.png'
    setTimeout(function() {
      console.log('go')
      that.$router.push({ path: '/cover' })
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