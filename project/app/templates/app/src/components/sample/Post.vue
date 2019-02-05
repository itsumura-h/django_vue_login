<template>
  <v-form>
    <v-text-field
      label="value1"
      v-model="value1"
      required
    ></v-text-field>
    <v-text-field
      label="value2"
      v-model="value2"
      required
    ></v-text-field>
    <v-btn @click="testPost" color="info">ボタン</v-btn>
  </v-form>
</template>

<script>
import Util from '../../common/Util';
import Const from '../../common/Const';
import API from '../../common/API';

export default {
  name: 'samplePost',
  data() {
    return {
      value1: '',
      value2: '',
    };
  },
  methods: {
    testPost() {
      const url = '/test/test6';
      const params = {
        value1: this.value1,
        value2: this.value2,
      };

      API.methods.postTest(url, params)
        .then((response) => {
          console.log(response);
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
};
</script>
