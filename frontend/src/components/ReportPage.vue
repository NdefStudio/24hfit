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
              @click="onClickBack"></x-icon>
    </x-header>

    <section class="main">
      <span class="button-label">条形图大小:</span>
      <input type="radio"
             name="resize-graph"
             id="graph-small" />
      <label for="graph-small">小</label>
      <input type="radio"
             name="resize-graph"
             id="graph-normal"
             checked="checked" />
      <label for="graph-normal">中</label>
      <input type="radio"
             name="resize-graph"
             id="graph-large" />
      <label for="graph-large">大</label>

      <span class="button-label">颜色:</span>
      <input type="radio"
             name="paint-graph"
             id="graph-blue"
             checked="checked" />
      <label for="graph-blue">Blue</label>
      <input type="radio"
             name="paint-graph"
             id="graph-green" />
      <label for="graph-green">Green</label>
      <input type="radio"
             name="paint-graph"
             id="graph-rainbow" />
      <label for="graph-rainbow">Rainbow</label>

      <span class="button-label">活动:</span>
      <input type="radio"
             name="fill-graph"
             id="f-none" />
      <label for="f-none">午休</label>
      <input type="radio"
             name="fill-graph"
             id="f-product1"
             checked="checked" />
      <label for="f-product1">冥想</label>
      <input type="radio"
             name="fill-graph"
             id="f-product2" />
      <label for="f-product2">睡眠</label>
      <input type="radio"
             name="fill-graph"
             id="f-product3" />
      <label for="f-product3">运动</label>

      <ul class="graph-container">
        <li>
          <span>02.25</span>
          <div class="bar-wrapper">
            <div class="bar-container">
              <div class="bar-background"></div>
              <div class="bar-inner">25</div>
              <div class="bar-foreground"></div>
            </div>
          </div>
        </li>
        <li>
          <span>02.26</span>
          <div class="bar-wrapper">
            <div class="bar-container">
              <div class="bar-background"></div>
              <div class="bar-inner">50</div>
              <div class="bar-foreground"></div>
            </div>
          </div>
        </li>
        <li>
          <span>02.27</span>
          <div class="bar-wrapper">
            <div class="bar-container">
              <div class="bar-background"></div>
              <div class="bar-inner">75</div>
              <div class="bar-foreground"></div>
            </div>
          </div>
        </li>
        <li>
          <span>02.28</span>
          <div class="bar-wrapper">
            <div class="bar-container">
              <div class="bar-background"></div>
              <div class="bar-inner">100</div>
              <div class="bar-foreground"></div>
            </div>
          </div>
        </li>
        <li>
          <span>02.29</span>
          <div class="bar-wrapper">
            <div class="bar-container">
              <div class="bar-background"></div>
              <div class="bar-inner">50</div>
              <div class="bar-foreground"></div>
            </div>
          </div>
        </li>
        <li>
          <ul class="graph-marker-container">
            <li style="bottom:25%;">
              <span>3</span>
            </li>
            <li style="bottom:50%;">
              <span>6</span>
            </li>
            <li style="bottom:75%;">
              <span>9</span>
            </li>
            <li style="bottom:100%;">
              <span>12</span>
            </li>
          </ul>
        </li>
      </ul>
    </section>
  </div>
</template>

<script>
import { XHeader } from 'vux'

export default {
  components: {
    XHeader
  },
  methods: {
    onClickBack() {
      this.$router.push(`/main/${this.id}/my`)
    }
  },
  data() {
    return {
      id: this.$route.params.id
    }
  }
}
</script>

<style>
@import '../assets/graph.css';
</style>