<template>
  <svg
    v-if="name === 'folder'"
    width="8"
    height="8"
    viewBox="0 0 8 8"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
  >
    <rect x="0.5" y="2.27783" width="7" height="5.22222" rx="0.5" />
    <path
      d="M1 0.5H2.55556C2.8317 0.5 3.05556 0.723857 3.05556 1V2.16667H0.5V1C0.5 0.723858 0.723858 0.5 1 0.5Z"
    />
  </svg>

  <svg
    v-else-if="name === 'document'"
    width="7"
    height="8"
    viewBox="0 0 7 8"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
  >
    <rect x="0.5" y="0.5" width="6" height="7" rx="1.5" />
    <line x1="1.83334" y1="2.21436" x2="5.16668" y2="2.21436" />
    <line x1="1.83334" y1="3.92847" x2="5.16668" y2="3.92847" />
    <line x1="1.83334" y1="5.64282" x2="5.16668" y2="5.64282" />
  </svg>

  <svg
    v-else-if="name === 'burger'"
    viewBox="0 0 32 32"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path d="M28,10H4A1,1,0,0,1,4,8H28a1,1,0,0,1,0,2Z" />
    <path d="M28,17H4a1,1,0,0,1,0-2H28a1,1,0,0,1,0,2Z" />
    <path d="M28,24H4a1,1,0,0,1,0-2H28a1,1,0,0,1,0,2Z" />
  </svg>

  <svg
    v-else-if="name === 'burger-cancel'"
    viewBox="0 0 32 32"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path
      d="M4,29a1,1,0,0,1-.71-.29,1,1,0,0,1,0-1.42l24-24a1,1,0,1,1,1.42,1.42l-24,24A1,1,0,0,1,4,29Z"
    />
    <path
      d="M28,29a1,1,0,0,1-.71-.29l-24-24A1,1,0,0,1,4.71,3.29l24,24a1,1,0,0,1,0,1.42A1,1,0,0,1,28,29Z"
    />
  </svg>
</template>

<script>
export default {
  props: ["name"],
};
</script>
