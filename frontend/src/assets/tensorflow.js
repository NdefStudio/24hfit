async function poseDection() {
  const imageScaleFactor = 1
  const flipHorizontal = false
  const outputStride = 16

  const imageElement = document.getElementById('cat')

  // 加载 posenet 模型
  const net = await posenet.load()

  const pose = await net.estimateSinglePose(
    imageElement,
    imageScaleFactor,
    flipHorizontal,
    outputStride
  )

  console.log(pose)
  document.write(pose)
}

function getMedia() {
  let constraints = {
    // 参数
    video: { width: 300, height: 300 },
    audio: false
  }
  // 获得video摄像头区域
  let video = document.getElementById('video')
  // 返回的Promise对象
  let promise = navigator.mediaDevices.getUserMedia(constraints)
  // then()异步，调用MediaStream对象作为参数
  promise.then(function(MediaStream) {
    video.srcObject = MediaStream
    video.play()
  })
}

function takePhoto() {
  // 获得Canvas对象
  let video = document.getElementById('video')
  let canvas = document.getElementById('canvas')
  let ctx = canvas.getContext('2d')
  // 绘图
  ctx.drawImage(video, 0, 0, 300, 300)
}
