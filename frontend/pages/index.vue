<template>
  <div class="flex flex-col items-center justify-center h-screen bg-gray-100">
    <div class="flex w-[80%] max-w-5xl bg-white rounded shadow-lg p-8 gap-6">
      <!-- Left: Input Section -->
      <div class="w-1/3">
        <h1 class="text-3xl font-bold mb-4">Ask a Question</h1>

        <!-- Input Field -->
        <input
          v-model="question"
          placeholder="Enter your question"
          class="p-2 border border-gray-300 rounded mb-4 w-full text-lg"
        />

        <!-- Ask Button -->
        <button
          @click="askQuestion"
          class="px-6 py-2 bg-blue-500 text-white rounded hover:bg-blue-700 transition-colors"
        >
          Ask
        </button>
      </div>

      <!-- Right: Streaming Response -->
      <div class="w-2/3 border-l pl-6">
        <h2 class="text-xl font-semibold mb-2">Response:</h2>
        <div
          ref="responseContainer"
          class="h-80 overflow-auto border p-4 rounded bg-gray-50"
        >
          <div v-for="(message, index) in messages" :key="index">
            <p class="text-lg text-gray-700 py-2">
              {{ message }}
            </p>
            <!-- Dark Bold Separator -->
            <hr
              v-if="index < messages.length - 1"
              class="border-t-2 border-gray-700 my-2"
            />
          </div>
        </div>
      </div>
    </div>

    <div
      class="flex w-[80%] max-w-5xl bg-white rounded shadow-lg p-8 gap-6"
    >
  
    <div class="w-full border-l pl-6">
        <h2 class="text-xl font-semibold mb-2">Detailed Response:</h2>
        <div
          ref="responseContainer"
          class="h-80 overflow-auto border p-4 rounded bg-gray-50"
        >
          <div v-for="(message, index) in messages" :key="index">
            <p class="text-lg text-gray-700 py-2">
              {{ message }}
            </p>
            <!-- Dark Bold Separator -->
            <hr
              v-if="index < messages.length - 1"
              class="border-t-2 border-gray-700 my-2"
            />
          </div>
        </div>
      </div>
  
  
  </div>
  </div>
</template>

<script>
import { io } from "socket.io-client";

export default {
  data() {
    return {
      question: "",
      messages: [],
      socket: null,
    };
  },
  methods: {
    askQuestion() {
      if (!this.question.trim()) return;

      this.messages = [];
      this.socket.emit("ask_question", { question: this.question });
    },
    autoScroll() {
      this.$nextTick(() => {
        const container = this.$refs.responseContainer;
        if (container) {
          container.scrollTop = container.scrollHeight;
        }
      });
    },
  },
  mounted() {
    this.socket = io("http://localhost:5000");

    this.socket.on("connect", () => {
      console.log("Connected to WebSocket server");
    });

    this.socket.on("stream_data", (data) => {
      this.messages.push(data);
      this.autoScroll();
    });

    this.socket.on("disconnect", () => {
      console.log("Disconnected from WebSocket server");
    });
  },
  beforeUnmount() {
    if (this.socket) {
      this.socket.disconnect();
    }
  },
};
</script>
