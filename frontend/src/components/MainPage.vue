<template>
  <div>
    <x-header>
      <span>24hFit</span>
      <x-icon slot="overwrite-left"
              type="navicon"
              size="35"
              style="fill:#fff;position:relative;top:-8px;left:-3px;"
              @click="onClickDrawer"></x-icon>
    </x-header>
    <!--    <tabbar @on-index-change="onIndexChange">
      <tabbar-item>
        <img slot="icon"
             src="../assets/demo/icon_nav_button.png">
        <img slot="icon-active"
             src="../assets/demo/icon_nav_msg.png">
        <span slot="label">one</span>
      </tabbar-item>
      <tabbar-item>
        <img slot="icon"
             src="../assets/demo/icon_nav_article.png">
        <img slot="icon-active"
             src="../assets/demo/icon_nav_cell.png">
        <span slot="label">two</span>
      </tabbar-item>
    </tabbar>
    -->
    <router-view></router-view>
    <tabbar @on-index-change="onTabChange">
      <tabbar-item>
        <span slot="label">事务</span>
      </tabbar-item>
      <tabbar-item>
        <span slot="label">帖子</span>
      </tabbar-item>
      <tabbar-item>
        <span slot="label">我</span>
      </tabbar-item>
    </tabbar>
  </div>
</template>

<script>
import { XHeader, Tabbar, TabbarItem } from 'vux'

export default {
  components: {
    XHeader,
    Tabbar,
    TabbarItem
  },
  data() {
    return {
      draweropen: false
    }
  },
  methods: {
    onClickDrawer() {
      this.draweropen = !this.draweropen
      console.log(this.draweropen)
    },
    onTabChange(oldindex, newindex) {
      console.log(oldindex, newindex)
      if ((newindex = 0)) this.$router.push('/main/routine')
      else if ((newindex = 1)) this.$router.push('/main')
      else if ((newindex = 2)) this.$router.push('/main/my') //uncaught exception:object
    }
  }
}
</script>

<style>
</style>