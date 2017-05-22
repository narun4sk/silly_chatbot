// Register components
Vue.component('chatarea', {
  delimiters: ['${', '}'],
  props: ['messages'],
  template: '<textarea readonly="" rows="20">${messages}</textarea>',
});


// Create a root instance
var app = new Vue({
  el: '#app',
  delimiters: ['${', '}'],

  data: {
      messages: [
        'Type "@tellme help", to see supported commands.',
        'Long time no see !!',
      ],
      usr: '',
  },

  methods: {
    // Handle form
    on_submit: function() {
      var that = this;
      input = that.usr.trim();
      if (input) {
        // Update message log
        that.messages.push(input);
        // Reset user input immediately
        that.usr = '';
        // Now let's talk to our Bot
        $.get("/askmeanything/", {q: input}).done(function(data) {
          if (data.response) {
            // Update message log with bot's thoughts...
            that.messages.push(data.response);
          }
        });
      }
    }
  },

  computed: {
    // Re-generate message log every time it is updated
    // Show the newest messages on the top
    msg_log: function () {
      var msg = this.messages.slice();
      return msg.reverse().join('\n');
    }
  }

});