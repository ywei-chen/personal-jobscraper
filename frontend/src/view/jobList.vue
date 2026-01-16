<!-- 首頁職缺列表 -->

<script setup>
import router from '@/router';
import axios from 'axios';
import { ref, onMounted } from 'vue';


const jobs = ref([])
const loading = ref(true)
const error = ref(null)

// Axios call API 取得jobs data
const fectchJob = async () => {
    try {
        const res = await axios.get('http://127.0.0.1:8000/jobs')
        jobs.value = res.data
    } catch (e) {
        error.value = `無法取得資料`
        console.log(e.message)
    } finally {
        loading.value = false
    }
}

// onClik goto jobDetail
const gotoDetail = (jobID) => {
    router.push(`/jobs/${jobID}`)
}

onMounted(() => {
    fectchJob()
})
</script>

<template>
    <div class="min-h-screen bg-stone-200 py-10">
        <div class="max-w-4xl mx-auto p-6 bg-stone-50 rounded-xl shadow-sm">
            <h1 class="text-3xl font-bold mb-8 text-center text-stone-800">
                職缺列表
            </h1>
            <div v-if="loading" class="text-center text-stone-500">
                頁面載入中...
            </div>
            <div v-else-if="error" class="text-red-600 text-center">
                {{ error }}
            </div>
            <div v-else>
                <div v-if="jobs.length === 0" class="text-center text-stone-500">
                    目前沒有職缺資料
                </div>
                <template v-else>
                    <div v-for="job in jobs" :key="job.id" @click="gotoDetail(job.id)" class="
                        border border-stone-300
                        bg-white
                        rounded-lg
                        p-5
                        mb-4
                        cursor-pointer
                        hover:shadow-md
                        hover:-translate-y-0.5
                        transition
                        ">
                        <h2 class="text-xl font-semibold text-blue-700">
                            {{ job.name }}
                        </h2>
                        <p class="text-stone-700 mt-1">
                            {{ job.company }}
                        </p>
                        <p class="flex gap-4 mt-2 text-sm text-stone-500">
                            <span>{{ job.addr }}</span>
                            <span>{{ job.salary }}</span>
                        </p>
                    </div>
                </template>
            </div>
        </div>
    </div>
</template>
