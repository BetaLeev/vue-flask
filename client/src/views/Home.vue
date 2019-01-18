<template>
  <div class="container">

    <div class="row">
      <div class="col">
        <h1>单词大会</h1>
        <hr><br><br>
        <alert :message=message
          v-if="showMessage"></alert>
        <button type="button"
          class="btn btn-success btn-sm"
          v-b-modal.word-modal>添加单词</button>
        <br><br>

        <!-- word table -->
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">单词</th>
              <th scope="col">词性</th>
              <th scope="col">释义</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(item, index) in word"
              :key="index">
              <td>{{ item.单词 }}</td>
              <td> {{item.词性}} </td>
              <td>
                {{ item.释意 }}
              </td>
              <td>
                <button type="button"
                  class="btn btn-warning btn-sm"
                  v-b-modal.word-update-modal
                  @click="editWord(item)">
                  修改
                </button>
                <button type="button"
                  class="btn btn-danger btn-sm"
                  @click="onDeleteWord(item)">
                  删除
                </button>
              </td>
            </tr>
          </tbody>
        </table>

      </div>
    </div>

    <!-- add word modal -->
    <b-modal ref="addWordModal"
      id="word-modal"
      title="加入一个单词"
      hide-footer>
      <b-form @submit="onSubmit"
        @reset="onReset"
        class="w-100">
        <b-form-group id="form-word-group"
          label="单词:"
          label-for="form-word-input">
          <b-form-input id="form-word-input"
            type="text"
            autocomplete="off"
            v-model="addWordForm.word"
            required
            placeholder="输入单词">
          </b-form-input>

        </b-form-group>
        <b-form-group id="form-type-group"
          label="词性:"
          label-for="form-type-input">
          <b-form-input id="form-type-input"
            type="text"
            autocomplete="off"
            v-model="addWordForm.type"
            required
            placeholder="输入词性">
          </b-form-input>
        </b-form-group>

        <b-form-group id="form-mean-group"
          label="释义:"
          autocomplete="off"
          label-for="form-mean-input">
          <b-form-input id="form-mean-input"
            type="text"
            v-model="addWordForm.mean"
            required
            placeholder="输入释义">
          </b-form-input>
        </b-form-group>
        <b-button type="submit"
          variant="primary">添加</b-button>
        <b-button type="reset"
          variant="danger">取消</b-button>
      </b-form>
    </b-modal>

    <b-modal ref="editWordModal"
      id="word-update-modal"
      title="修改"
      hide-footer>
      <b-form @submit="onSubmitUpdate"
        @reset="onResetUpdate"
        class="w-100">
        <b-form-group id="form-word-edit-group"
          label="单词:"
          label-for="form-word-edit-input">
          <b-form-input id="form-word-edit-input"
            type="text"
            v-model="editForm.单词"
            autocomplete="off"
            required
            placeholder="修改单词拼写">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-type-edit-group"
          label="词性:"
          label-for="form-type-edit-input">
          <b-form-input id="form-type-edit-input"
            type="text"
            autocomplete="off"
            v-model="editForm.词性"
            required
            placeholder="修改词性">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-mean-edit-group"
          label="释义:"
          label-for="form-mean-edit-input">
          <b-form-input id="form-mean-edit-input"
            type="text"
            autocomplete="off"
            v-model="editForm.释意"
            required
            placeholder="修改释义">
          </b-form-input>
        </b-form-group>
        <b-button type="submit"
          variant="primary">更新</b-button>
        <b-button type="reset"
          variant="danger">取消</b-button>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from "axios";
import Alert from "@/components/Alert";

export default {
  data() {
    return {
      word: [],
      addWordForm: {
        word: "",
        mean: "",
        type: ""
      },
      editForm: {
        id: "",
        word: "",
        mean: "",
        type: ""
      },
      message: "",
      showMessage: false
    };
  },
  components: {
    alert: Alert
  },

  methods: {
    getWord() {
      const path = "/api/word";
      axios
        .get(path)
        .then(res => {
          this.word = res.data.word;
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addWord(payload) {
      const path = "api/word";
      axios
        .post(path, payload)
        .then(() => {
          this.getWord();
          this.message = "单词已经添加成功!";
          this.showMessage = true;
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
          this.getWord();
        });
    },
    updateWord(payload, wordID) {
      const path = `api/word/${wordID}`;
      axios
        .put(path, payload)
        .then(() => {
          this.getWord();
          this.message = "单词已经更新!";
          this.showMessage = true;
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
          this.getWord();
        });
    },
    removeWord(wordID) {
      const path = `api/word/${wordID}`;
      axios
        .delete(path)
        .then(() => {
          this.getWord();
          this.message = "删除成功!";
          this.showMessage = true;
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
          this.getWord();
        });
    },
    initForm() {
      this.addWordForm.word = "";
      this.addWordForm.type = "";
      this.addWordForm.mean = "";
      this.editForm.id = "";
      this.editForm.word = "";
      this.editForm.type = "";
      this.editForm.mean = "";
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addWordModal.hide();
      const payload = {
        word: this.addWordForm.word,
        type: this.addWordForm.type,
        mean: this.addWordForm.mean
      };
      this.addWord(payload);
      this.initForm();
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editWordModal.hide();
      const payload = {
        word: this.editForm.单词,
        type: this.editForm.词性,
        mean: this.editForm.释意
      };
      console.log(payload);
      this.updateWord(payload, this.editForm.id);
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addWordModal.hide();
      this.initForm();
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editWordModal.hide();
      this.initForm();
      this.getWord();
    },
    onDeleteWord(word) {
      this.removeWord(word.id);
    },
    editWord(word) {
      this.editForm = word;
      console.log(this.editForm);
    }
  },
  created() {
    this.getWord();
  }
};
</script>
<style scoped>
h1 {
  text-align: center;
}
</style>

