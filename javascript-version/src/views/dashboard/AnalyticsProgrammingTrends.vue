<script setup>
import { ref, onMounted, computed } from 'vue'
import programmingData from '@/data/programming-stats.json'
import VueApexCharts from 'vue3-apexcharts'

const languages = ref([])

onMounted(() => {
  languages.value = programmingData.languages
})

const series = computed(() => {
  return languages.value.map(lang => ({
    name: lang.name,
    data: lang.trend.lastYear
  }))
})

const chartOptions = computed(() => {
  return {
    chart: {
      height: 350,
      type: 'line',
      zoom: {
        enabled: false
      },
      toolbar: {
        show: false
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      width: 2,
      curve: 'smooth'
    },
    grid: {
      row: {
        colors: ['transparent', 'transparent'],
        opacity: 0.5
      }
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    },
    yaxis: {
      title: {
        text: 'Popularity Score'
      }
    },
    tooltip: {
      y: {
        formatter: val => val + '%'
      }
    },
    legend: {
      position: 'top',
      horizontalAlign: 'right',
      floating: true,
      offsetY: -25,
      offsetX: -5
    }
  }
})
</script>

<template>
  <VCard>
    <VCardItem>
      <VCardTitle>Language Popularity Trends</VCardTitle>
      <template #append>
        <div class="text-caption">
          Last 12 Months
        </div>
      </template>
    </VCardItem>

    <VCardText>
      <VueApexCharts
        :options="chartOptions"
        :series="series"
        height="350"
      />
    </VCardText>
  </VCard>
</template> 