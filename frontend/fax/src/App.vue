<template>
  <div>
    <div><strong>Likes: {{ likes }}</strong></div>
    <div><strong>Dislikes: {{ dislikes }}</strong></div>
  </div>
</template>

<script>
export default {
  data() {
    return  {
      likes: 0,
      dislikes: 0,
    }
  }
}

</script>

<style>

</style>
