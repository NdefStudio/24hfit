<template>
  <div style="height:100%">
    <x-header slot="header"
              style="width:100%;position:fixed;
              left:0;top:0;z-index:100;background-color:#43c9db;">
      <span>健康管理报告</span>
      <x-icon slot="overwrite-left"
              type="ios-arrow-back"
              size="35"
              style="fill:#fff;position:relative;top:-8px;left:-3px;"
              @click="onClickDrawer"></x-icon>
    </x-header>
  </div>
</template>

<script>
import { XHeader } from 'vux'

export default {
  components: {
    XHeader
  },
  data() {
    return {}
  }
}
</script>

<style>
</style>