# Brave Browser

This role handles configuring the Brave Browser repository and then install
Brave Browser.

## Requirements

The hosts you are targeting should have the following packages:

- python >= 2.6
- python-dnf

## Role Variables

| Variable      | Required | Default   | Description                                                                |
| ------------- | -------- | --------- | -------------------------------------------------------------------------- |
| brave_channel | &#9989;  | `release` | The channel to use. Possible options are `release`, `beta`, and `nightly`. |

## Dependencies

None

## Example Playbook

```yaml
- hosts: servers
  roles:
    - role: jaredhocutt.brave_browser
      vars:
        brave_channel: beta
```

## License

MIT

## Author Information

Jared Hocutt (@jaredhocutt)
