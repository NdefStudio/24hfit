<template>
  <div>
    <view-box ref="viewBox"
              :body-padding-top="isShowNav ? '46px' : '0'"
              body-padding-bottom="55px">
      <x-header slot="header"
                style="width:100%;position:fixed;
              left:0;top:0;z-index:100;background-color:#43c9db;">
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
      <keep-alive>
        <router-view style="margin-top:70px;margin-bottom:100px;"></router-view>
      </keep-alive>
      <tabbar style="width:100%;position:fixed;
              left:0;z-index:100;"
              @on-index-change="onTabChange">
        <tabbar-item :link="{path:'/main/routine'}">
          <span slot="label">事务</span>
        </tabbar-item>
        <tabbar-item :link="{path:'/main/posts'}">
          <span slot="label">帖子</span>
        </tabbar-item>
        <tabbar-item :link="{path:'/main/my'}">
          <span slot="label">我</span>
        </tabbar-item>
      </tabbar>
    </view-box>
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
    }
  }
}
</script>

<style>
</style>