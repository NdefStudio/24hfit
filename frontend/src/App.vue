<template>
  <div id="app"
       style="height:100%">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style lang="less">
@import '~vux/src/styles/reset.less';

body {
  background-color: #e0f0f0;
}
</style>
