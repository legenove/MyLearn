/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var AlbumsAlbumId = function () {
    /*
        @params obj 'data params'
            album_id   'string' album id in path
            
        @success
            status 200    type:object
            date_updated   'ref' 
            date_created   'ref' 
            image   'string' 
            id   'string' 
            icon   'string' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/albums/" + obj.album_id + "",
            method: "GET",
            success: function (res) {
                typeof obj.success === 'function' && obj.success(res);
            },
            fail: function (res) {
                typeof obj.fail === 'function' && obj.fail(res);
            },
            complete: function (res) {
                typeof obj.complete === 'function' && obj.complete(res);
            }
        })
    };
    
    /*
        @params obj 'data params'
            album_id   'string' album id in path
            album_type   'string' 
            description   'string' 
            title   'string' 
            order_score   'integer' 
            is_free   'boolean' 
            _image   'string' 
            creator_id   'integer' 
            share_description   'string' 
            is_show_showcase   'boolean' 
            is_show_title   'boolean' 
            _icon   'string' 
            is_published   'boolean' 
            
        @success
            status 200    type:object
            date_updated   'ref' 
            date_created   'ref' 
            image   'string' 
            id   'string' 
            icon   'string' 
            
    */
    this.put = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/albums/" + obj.album_id + "",
            method: "PUT",
            data: {
                album_type: obj.album_type,
                description: obj.description,
                title: obj.title,
                order_score: obj.order_score,
                is_free: obj.is_free,
                _image: obj._image,
                creator_id: obj.creator_id,
                share_description: obj.share_description,
                is_show_showcase: obj.is_show_showcase,
                is_show_title: obj.is_show_title,
                _icon: obj._icon,
                is_published: obj.is_published
                },
            success: function (res) {
                typeof obj.success === 'function' && obj.success(res);
            },
            fail: function (res) {
                typeof obj.fail === 'function' && obj.fail(res);
            },
            complete: function (res) {
                typeof obj.complete === 'function' && obj.complete(res);
            }
        })
    };
    

};

module.exports = {
    AlbumsAlbumId: new AlbumsAlbumId
};