var swift = {
    models: [],
    views: [],
    init: function (params) {
        params = params || {};
        swift.models.UserModel = Backbone.Model.extend({
            defaults: {
                userid: null,
                username: null,
                email: null
            }
        });
        
        swift.models.UserCollection = Backbone.Collection.extend({
            url: '/users',
            model: swift.models.UserModel,
            parse: function(data) {
                return data.users;
            },
            initialize: function () {
                console.log(this.collection);
            }
        });
        
        swift.views.usersListView = Backbone.View.extend({
            el: '#UsersList'
        });
        
        swift.views.usersListItemView = Backbone.View.extend({
            tagName: 'li',
            className: 'user',
            initialize: function () {
                console.log('list item');
                console.log(this.model);
            }
        });
    }
};


swift.init();
var tempModel = new swift.models.UserModel();
var users = new swift.models.UserCollection();
var usersListView = null;
users.fetch().then(function () {
    usersListView = new swift.views.usersListView({ collection: users });
    console.log(users);
})
var usersListItemView = new swift.views.usersListItemView({ model: tempModel});



// usersListView.$el.append('<li>hello</li>');
// var users = new swift.models.UserCollection();

// users.fetch().then(function () {
//     _.each(users, function(item, index) {
//         console.log(users.at(index));
//     })
// })

// users.create({username: 'paul', email: 'paul@swift.com'});
// 
// console.log(users.findWhere({username: 'paul'}));
